"""
Configuration module for the Woodblock Data Augmentation pipeline.

All configurable parameters are stored here.
Avoid hardcoded values in other files.
"""

import os

# ---------------------------------------------------------------------------
# Directory paths
# ---------------------------------------------------------------------------
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR: str = os.path.join(BASE_DIR, "data", "input")
OUTPUT_DIR: str = os.path.join(BASE_DIR, "data", "output")

# ---------------------------------------------------------------------------
# Dataset settings
# ---------------------------------------------------------------------------
SUPPORTED_EXTENSIONS: tuple[str, ...] = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
SAMPLES_PER_IMAGE: int = 5

# ---------------------------------------------------------------------------
# Image size
# ---------------------------------------------------------------------------
IMAGE_WIDTH: int = 512
IMAGE_HEIGHT: int = 512

# ---------------------------------------------------------------------------
# Augmentation probabilities
# ---------------------------------------------------------------------------
ROTATE_PROBABILITY: float = 0.5
BLUR_PROBABILITY: float = 0.3
BRIGHTNESS_PROBABILITY: float = 0.5
CONTRAST_PROBABILITY: float = 0.5
GAMMA_PROBABILITY: float = 0.3
NOISE_PROBABILITY: float = 0.4
PERSPECTIVE_PROBABILITY: float = 0.3
RESIZE_PROBABILITY: float = 0.0

# ---------------------------------------------------------------------------
# Rotation parameters
# ---------------------------------------------------------------------------
ROTATE_LIMIT: int = 10
ROTATE_BORDER_MODE: int = 0  # cv2.BORDER_CONSTANT

# ---------------------------------------------------------------------------
# Blur parameters
# ---------------------------------------------------------------------------
BLUR_LIMIT: tuple[int, int] = (3, 7)

# ---------------------------------------------------------------------------
# Brightness parameters
# ---------------------------------------------------------------------------
BRIGHTNESS_LIMIT: tuple[float, float] = (-0.2, 0.2)

# ---------------------------------------------------------------------------
# Contrast parameters
# ---------------------------------------------------------------------------
CONTRAST_LIMIT: tuple[float, float] = (-0.2, 0.2)

# ---------------------------------------------------------------------------
# Gamma parameters
# ---------------------------------------------------------------------------
GAMMA_LIMIT: tuple[float, float] = (80.0, 120.0)

# ---------------------------------------------------------------------------
# Noise parameters
# ---------------------------------------------------------------------------
NOISE_VAR_LIMIT: tuple[float, float] = (0.01, 0.05)

# ---------------------------------------------------------------------------
# Perspective parameters
# ---------------------------------------------------------------------------
PERSPECTIVE_SCALE: tuple[float, float] = (0.02, 0.05)

# ---------------------------------------------------------------------------
# Resize parameters
# ---------------------------------------------------------------------------
RESIZE_WIDTH: int = IMAGE_WIDTH
RESIZE_HEIGHT: int = IMAGE_HEIGHT
