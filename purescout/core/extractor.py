"""
Scene Feature Extractor
Extract 5D dynamic scene features from creator videos using OpenCV.
"""

import cv2
import numpy as np
from typing import List, Optional


class SceneFeatureExtractor:
    """
    Extract 5-dimensional scene features from video:
    0. trajectory_curvature
    1. velocity_gradient
    2. dynamic_range
    3. terrain_complexity
    4. camera_motion_amplitude
    """

    FEATURE_DIM = 5
    FEATURE_NAMES = [
        "trajectory_curvature",
        "velocity_gradient",
        "dynamic_range",
        "terrain_complexity",
        "camera_motion_amplitude",
    ]

    def __init__(
        self,
        sample_interval: int = 5,
        max_frames: int = 300,
        edge_threshold: float = 50,
        lowlight_threshold: float = 80,
    ):
        self.sample_interval = sample_interval
        self.max_frames = max_frames
        self.edge_threshold = edge_threshold
        self.lowlight_threshold = lowlight_threshold

    def extract_from_video(self, video_path: str) -> np.ndarray:
        """Extract feature vector from a single video file."""
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")

        prev_gray = None
        flow_magnitudes = []
        flow_angle_diffs = []
        frame_count = 0
        total_frames = 0
        total_lowlight_frames = 0
        edge_densities = []

        while True:
            ret, frame = cap.read()
            if not ret or frame_count >= self.max_frames:
                break

            if frame_count % self.sample_interval != 0:
                frame_count += 1
                continue

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            total_frames += 1

            # Optical flow calculation
            if prev_gray is not None:
                flow = cv2.calcOpticalFlowFarneback(
                    prev_gray, gray, None,
                    pyr_scale=0.5, levels=3, winsize=15,
                    iterations=3, poly_n=5, poly_sigma=1.2, flags=0
                )
                mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
                flow_magnitudes.append(np.mean(mag))
                flow_angle_diffs.append(np.std(ang))

            # Low-light detection
            if np.mean(gray) < self.lowlight_threshold:
                total_lowlight_frames += 1

            # Edge density for terrain complexity
            edges = cv2.Canny(gray, self.edge_threshold, self.edge_threshold * 2)
            edge_density = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
            edge_densities.append(edge_density)

            prev_gray = gray.copy()
            frame_count += 1

        cap.release()

        if len(flow_magnitudes) == 0:
            return np.array([0.1, 0.1, 0.3, 0.2, 0.1], dtype=np.float32)

        features = np.array([
            np.clip(np.mean(flow_angle_diffs) * 2.0, 0, 1),
            np.clip(np.std(flow_magnitudes) * 3.0, 0, 1),
            np.clip(total_lowlight_frames / max(total_frames, 1), 0, 1),
            np.clip(np.mean(edge_densities) * 5.0, 0, 1),
            np.clip(np.mean(flow_magnitudes) * 2.0, 0, 1),
        ], dtype=np.float32)

        return features
