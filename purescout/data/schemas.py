"""
Data schemas for creators and collaboration feedback.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CreatorProfile:
    id: str
    name: str
    video_paths: List[str]
    avg_scene_features: Optional[List[float]] = None
    match_matrix: Optional[dict] = None


@dataclass
class CollaborationFeedback:
    creator_id: str
    product_function: str
    actual_playback: int
    actual_conversion: float
    engagement_rate: float
    content_quality_score: float
