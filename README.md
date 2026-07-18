# PureScout-AI

AI-powered creator content simulation engine for action camera brands. Predict which creator can maximize your product's features before you sign them. Built for Insta360 Think Bold spirit.

[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![Framework PyTorch](https://img.shields.io/badge/framework-PyTorch-ee4c2c.svg)](https://pytorch.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-blue.svg)](https://opencv.org/)

## Overview

PureScout-AI is an open-source content potential simulation and co-creation decision engine designed for action camera brands.

It moves beyond conventional influencer scoring systems by using computer vision to extract dynamic scene features from creator videos and calculate match potential with product capabilities.

## Core Capabilities

| Module | Function | Technology |
|--------|----------|------------|
| Scene Feature Extraction | Extract 5D dynamic features from creator videos: trajectory curvature, velocity gradient, dynamic range, terrain complexity, camera motion amplitude | OpenCV optical flow + Canny edge detection |
| Capability Matching Matrix | Matrix operation between creator features and product specs, output potential index (0-1) | PyTorch + Sigmoid |
| Batch Analysis | Parallel analysis with cache support | NumPy + file cache |
| Feedback Fine-tuning | Optimize matching weights based on real collaboration data | PyTorch fine-tuning + MSE Loss |
| Report Generation | Auto-generate ranking, radar charts, heatmaps, HTML/PDF reports | Matplotlib |

## Installation

```bash
git clone https://github.com/ricartomhao/PureScout-AI.git
cd PureScout-AI
pip install -r requirements.txt
pip install -e .
```

## Usage

### Command Line Interface

```bash
# Run full pipeline demo
python main.py --mode demo

# Analyze a single creator
python main.py --mode analyze --creator-id <id> --video-dir <path>

# Batch analysis from JSON
python main.py --mode batch --creators-file <path> --export-json <path>

# Fine-tune model with feedback data
python main.py --mode train --feedback-file <path>

# Export HTML report
python main.py --mode export --export-json <path> --export-html <path>
```

### Python API

```python
from purescout.core.extractor import SceneFeatureExtractor
from purescout.core.mapper import CapabilityFunctionMapper
from purescout.core.analyzer import PureScoutAnalyzer
from purescout.data.schemas import CreatorProfile

# Configure product feature requirement matrix
product_specs = {
    "360_Stitching": [0.9, 0.4, 0.5, 0.8, 0.9],
    "Invisible_Selfie_Stick": [0.9, 0.8, 0.3, 0.7, 0.9],
    "FlowState_Stabilization": [0.4, 0.7, 0.3, 0.9, 1.0],
    "PureVideo_LowLight": [0.1, 0.1, 1.0, 0.2, 0.3],
}

extractor = SceneFeatureExtractor()
mapper = CapabilityFunctionMapper(product_specs)
analyzer = PureScoutAnalyzer(mapper, extractor)

creator = CreatorProfile(id="C001", name="creator_name", video_paths=["./videos/sample.mp4"])
result = analyzer.analyze_creator(creator)

for func, score in result.match_matrix.items():
    print(f"{func}: {score*100:.1f}%")
```

## CLI Modes

| Mode | Description |
|------|-------------|
| demo | Run complete pipeline with simulated data |
| analyze | Analyze individual creator from video directory |
| batch | Batch process creators from JSON file |
| train | Fine-tune model using feedback data |
| export | Export analysis results to HTML report |

## Architecture

```
                    [ Creator Historical Videos ]
                               |
                               v
              +-----------------------------+
              |  SceneFeatureExtractor      |  <- Extract 5D scene features
              |    (OpenCV Optical Flow)    |
              +--------------+--------------+
                               |
                               v
              +-----------------------------+
              |  CapabilityFunctionMapper   |  <- Matrix operation: W @ v
              |    (PyTorch)                |
              +--------------+--------------+
                               |
                               v
              +-----------------------------+
              |  Match Potential Prediction |  <- Output capability scores
              |    (0-1 index)              |
              +--------------+--------------+
                               |
                               v
              +-----------------------------+
              |  Collaboration Execution    |  <- Think Bold co-creation
              +--------------+--------------+
                               |
                               v
              +-----------------------------+
              |  Real Performance Feedback  |  <- Playback / Conversion / Quality
              |    (Collaboration Data)     |
              +--------------+--------------+
                               |
                               v
              +-----------------------------+
              |  Model Fine-tuning          |  <- Gradient descent optimization
              |    (PyTorch)                |
              +-----------------------------+
```

## Project Structure

```
PureScout-AI/
├── .github/
│   └── workflows/
│       └── ci.yml
├── purescout/
│   ├── __init__.py
│   ├── core/
│   │   ├── extractor.py
│   │   ├── mapper.py
│   │   └── analyzer.py
│   ├── models/
│   │   └── product_configs.py
│   ├── data/
│   │   ├── schemas.py
│   │   └── loader.py
│   ├── pipeline/
│   │   └── processor.py
│   ├── viz/
│   │   ├── plots.py
│   │   └── report_builder.py
│   └── cli/
│       └── commands.py
├── tests/
├── examples/
├── data/
├── reports/
├── cache/
├── main.py
├── requirements.txt
├── setup.py
├── Makefile
└── README.md
```

## Feature Dimensions

| Feature | Description | Extraction Method |
|---------|-------------|-------------------|
| Trajectory Curvature | Path bending degree | Optical flow angle variance |
| Velocity Gradient | Speed change intensity | Optical flow magnitude std |
| Dynamic Range | Low-light scene ratio | Luminance histogram |
| Terrain Complexity | Edge density in scene | Canny edge detection |
| Camera Motion Amplitude | Camera shake intensity | Mean optical flow magnitude |

## Matching Score Calculation

```
score = Sigmoid(W @ v + b)

where:
  W = Product feature requirement matrix (n_features x 5)
  v = Creator scene feature vector (5 x 1)
  b = Bias term (trainable)
```

## Expected Impact

| Metric | Expected Outcome |
|--------|------------------|
| Screening Efficiency | From weekly manual to hourly AI screening, coverage from hundreds to tens of thousands |
| Match Accuracy | 30%+ improvement through continuous fine-tuning |
| Content Reuse | Results applied across website, social media, e-commerce |
| Decision Cost | Reduced trial-and-error spending via potential index + creative direction |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add some amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Insta360 Think Bold co-creation philosophy
- OpenCV computer vision library
- PyTorch deep learning framework

## Links

- Author: [@ricartomhao](https://github.com/ricartomhao)
- Repository: [https://github.com/ricartomhao/PureScout-AI](https://github.com/ricartomhao/PureScout-AI)
