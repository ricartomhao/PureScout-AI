from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="purescout-ai",
    version="0.1.0",
    author="ricartomhao",
    description="AI-powered creator content potential simulation engine for action camera brands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ricartomhao/PureScout-AI",
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.0.0",
        "torchvision>=0.15.0",
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "Pillow>=10.0.0",
        "tqdm>=4.65.0",
    ],
    entry_points={
        "console_scripts": [
            "purescout=purescout.cli.commands:main",
        ],
    },
)
