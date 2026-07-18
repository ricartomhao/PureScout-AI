"""
Quick start example for PureScout-AI.
"""

from purescout.core.extractor import SceneFeatureExtractor
from purescout.core.mapper import CapabilityFunctionMapper
from purescout.core.analyzer import PureScoutAnalyzer
from purescout.data.schemas import CreatorProfile

product_specs = {
    "360_Stitching": [0.9, 0.4, 0.5, 0.8, 0.9],
    "Invisible_Selfie_Stick": [0.9, 0.8, 0.3, 0.7, 0.9],
    "FlowState_Stabilization": [0.4, 0.7, 0.3, 0.9, 1.0],
    "PureVideo_LowLight": [0.1, 0.1, 1.0, 0.2, 0.3],
}

extractor = SceneFeatureExtractor()
mapper = CapabilityFunctionMapper(product_specs)
analyzer = PureScoutAnalyzer(mapper, extractor)

print("PureScout-AI initialized successfully.")
print(f"Product functions: {list(product_specs.keys())}")
