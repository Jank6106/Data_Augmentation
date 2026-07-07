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
PIPELINE_1_SAMPLES: int = 4
PIPELINE_2_SAMPLES: int = 2
SAMPLES_PER_IMAGE: int = PIPELINE_1_SAMPLES + PIPELINE_2_SAMPLES

# ---------------------------------------------------------------------------
# Image size
# ---------------------------------------------------------------------------
IMAGE_WIDTH: int = 512
IMAGE_HEIGHT: int = 512

# ---------------------------------------------------------------------------
# Augmentation probabilities
# ---------------------------------------------------------------------------
ROTATE_PROBABILITY: float = 0.6
BLUR_PROBABILITY: float = 0.5
BRIGHTNESS_PROBABILITY: float = 0.7
CONTRAST_PROBABILITY: float = 0.6
GAMMA_PROBABILITY: float = 0.4
NOISE_PROBABILITY: float = 0.5
PERSPECTIVE_PROBABILITY: float = 0.7
RESIZE_PROBABILITY: float = 0.0
# LIGHTING_BLOCK_PROBABILITY: float = 1.0
MOTION_BLUR_PROBABILITY: float = 0.3
SALT_PEPPER_PROBABILITY: float = 0.3
ELASTIC_PROBABILITY: float = 0.2
CLAHE_PROBABILITY: float = 0.5

# ---------------------------------------------------------------------------
# Rotation parameters
# ---------------------------------------------------------------------------
ROTATE_LIMIT: int = 10
ROTATE_BORDER_MODE: int = 0  # cv2.BORDER_CONSTANT
ROTATE_BORDER_VALUE: tuple[int, int, int] = (255, 255, 255)

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
NOISE_VAR_LIMIT: tuple[float, float] = (0.03, 0.06)

# ---------------------------------------------------------------------------
# Perspective parameters
# ---------------------------------------------------------------------------
PERSPECTIVE_SCALE: tuple[float, float] = (0.02, 0.05)

# ---------------------------------------------------------------------------
# Lighting Gradient parameters
# ---------------------------------------------------------------------------
GRADIENT_PROBABILITY: float = 1.0
GRADIENT_INTENSITY: tuple[float, float] = (0.3, 1.0)   # mức chênh lệch sáng tối
GRADIENT_DIRECTION: tuple[float, float] = (0.3, 1.0)   # xác suất ngang/dọc

# ---------------------------------------------------------------------------
# Resize parameters
# ---------------------------------------------------------------------------
RESIZE_WIDTH: int = IMAGE_WIDTH
RESIZE_HEIGHT: int = IMAGE_HEIGHT

# ---------------------------------------------------------------------------
# Motion Blur parameters
# ---------------------------------------------------------------------------
MOTION_BLUR_LIMIT: tuple[int, int] = (3, 7)

# ---------------------------------------------------------------------------
# Salt & Pepper parameters
# ---------------------------------------------------------------------------
SALT_PEPPER_AMOUNT: tuple[float, float] = (0.01, 0.04)
SALT_PEPPER_VS_PEPPER: tuple[float, float] = (0.4, 0.6)

# ---------------------------------------------------------------------------
# Elastic Transform parameters
# ---------------------------------------------------------------------------
ELASTIC_ALPHA: float = 1.0
ELASTIC_SIGMA: float = 50.0
ELASTIC_BORDER_MODE: int = 0  # cv2.BORDER_CONSTANT
ELASTIC_BORDER_VALUE: tuple[int, int, int] = (255, 255, 255)

# ---------------------------------------------------------------------------
# CLAHE parameters
# ---------------------------------------------------------------------------
CLAHE_CLIP_LIMIT: tuple[float, float] = (1.0, 4.0)
CLAHE_TILE_GRID_SIZE: tuple[int, int] = (8, 8)
