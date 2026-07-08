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

# Sample generation counts for each pipeline
PIPELINE_1_SAMPLES: int = 3
PIPELINE_2_SAMPLES: int = 3
PIPELINE_3_SAMPLES: int = 2
SAMPLES_PER_IMAGE: int = PIPELINE_1_SAMPLES + PIPELINE_2_SAMPLES + PIPELINE_3_SAMPLES

# ---------------------------------------------------------------------------
# Image size and resizing settings
# ---------------------------------------------------------------------------
IMAGE_WIDTH: int = 512
IMAGE_HEIGHT: int = 512
RESIZE_PROBABILITY: float = 0.0

# ---------------------------------------------------------------------------
# Augmentation border / noise defaults
# ---------------------------------------------------------------------------
# Border mode (0 corresponds to cv2.BORDER_CONSTANT)
BORDER_MODE: int = 0
BORDER_VALUE: tuple[int, int, int] = (255, 255, 255)

# Salt & Pepper ratio
SALT_PEPPER_VS_PEPPER: tuple[float, float] = (0.5, 0.8)

# ===========================================================================
# Pipeline Specific Parameters
# ===========================================================================

# Pipeline 1: Lighting simulation (Mô phỏng ánh sáng)
PIPELINE_1_GAMMA_LIMIT: tuple[float, float] = (80.0, 120.0)      # 0.8 to 1.2
PIPELINE_1_BRIGHTNESS_LIMIT: tuple[float, float] = (-0.2, 0.2)   # 0.8 to 1.2
PIPELINE_1_CONTRAST_LIMIT: tuple[float, float] = (-0.2, 0.2)     # 0.8 to 1.2
PIPELINE_1_GRADIENT_INTENSITY: tuple[float, float] = (0.3, 0.5)
PIPELINE_1_GRADIENT_DIRECTION: tuple[float, float] = (0.1, 0.25)

# Pipeline 2: Angle/Warp simulation (Mô phỏng góc chụp/cong vênh)
PIPELINE_2_ROTATE_LIMIT: int = 10                                # -10 to 10 degrees
PIPELINE_2_PERSPECTIVE_SCALE: tuple[float, float] = (0.02, 0.05) # Shift < 0.1
PIPELINE_2_ELASTIC_ALPHA: float = 25.0                           # Alpha 20-30
PIPELINE_2_ELASTIC_SIGMA: float = 4.5                            # Sigma 4-5

# Pipeline 3: Blur/Noise simulation (Mô phỏng mờ/nhiễu nền)
PIPELINE_3_BLUR_LIMIT: tuple[int, int] = (5, 5)                  # Kernel size (e.g. 5x5)
PIPELINE_3_NOISE_VAR_LIMIT: tuple[float, float] = (0.1, 0.2)     # Std range
PIPELINE_3_SALT_PEPPER_AMOUNT: tuple[float, float] = (0.03, 0.04) # Prob range
