"""
Batch analyzer for processing multiple creators.
"""

import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from purescout.core.extractor import SceneFeatureExtractor
from purescout.core.mapper import CapabilityFunctionMapper


class CreatorProfile:
    """Creator data container."""

    def __init__(
        self,
        id: str,
        name: str,
        video_paths: List[str],
        avg_scene_features: Optional[np.ndarray] = None,
        match_matrix: Optional[Dict[str, float]] = None,
    ):
        self.id = id
        self.name = name
        self.video_paths = video_paths
        self.avg_scene_features = avg_scene_features
        self.match_matrix = match_matrix


class PureScoutAnalyzer:
    """Batch analysis engine with caching support."""

    def __init__(
        self,
        mapper: CapabilityFunctionMapper,
        extractor: SceneFeatureExtractor,
        cache_dir: Optional[Path] = None,
    ):
        self.mapper = mapper
        self.extractor = extractor
        self.cache_dir = cache_dir
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)
        self._feature_cache = {}

    def analyze_creator(self, creator: CreatorProfile) -> CreatorProfile:
        """Analyze a single creator."""
        cache_key = creator.id
        if cache_key in self._feature_cache:
            scene_vector = self._feature_cache[cache_key]
        else:
            scene_vector = self.extractor.extract_from_creator(creator)
            self._feature_cache[cache_key] = scene_vector

        creator.avg_scene_features = scene_vector
        creator.match_matrix = self.mapper.get_creator_profile(scene_vector)
        return creator

    def rank_creators(
        self,
        creators: List[CreatorProfile],
        target_function: str,
    ) -> List[Tuple[CreatorProfile, float]]:
        """Rank creators by match score for a specific function."""
        scored = []
        for creator in creators:
            if creator.match_matrix is None:
                continue
            for func_name, score in creator.match_matrix.items():
                if target_function in func_name or func_name in target_function:
                    scored.append((creator, score))
                    break
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
