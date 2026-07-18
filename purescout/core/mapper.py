"""
Capability-Function Mapper
Match creator scene features with product capability requirements.
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Dict, List, Optional


class CapabilityFunctionMapper(nn.Module):
    """
    Match creator scene features with product capability requirements.
    score = Sigmoid(W @ v + b)
    """

    def __init__(
        self,
        product_features_config: Dict[str, List[float]],
        feature_dim: int = 5,
    ):
        super(CapabilityFunctionMapper, self).__init__()

        self.feature_names = list(product_features_config.keys())
        self.feature_dim = feature_dim

        init_matrix = np.array(
            [product_features_config[f] for f in self.feature_names],
            dtype=np.float32
        )
        self.product_matrix = nn.Parameter(torch.tensor(init_matrix))
        self.bias = nn.Parameter(torch.zeros(len(self.feature_names)))

    def forward(self, scene_vector: torch.Tensor) -> torch.Tensor:
        if scene_vector.dim() == 1:
            scene_vector = scene_vector.unsqueeze(0)
        scores = torch.matmul(scene_vector, self.product_matrix.T) + self.bias
        return torch.sigmoid(scores).squeeze(0)

    def get_creator_profile(self, scene_vector: np.ndarray) -> Dict[str, float]:
        with torch.no_grad():
            tensor = torch.tensor(scene_vector, dtype=torch.float32)
            scores = self.forward(tensor).numpy()
            return {name: float(score) for name, score in zip(self.feature_names, scores)}
