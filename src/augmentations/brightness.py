"""
Brightness augmentation module.

Simulates uneven illumination conditions during document capture.
"""

import albumentations as A

from src import config


def build(
    brightness_limit: tuple[float, float] | float | None = None,
    p: float | None = None,
) -> A.RandomBrightnessContrast:
    """Build a brightness-only transform.

    Uses RandomBrightnessContrast with contrast disabled so that
    brightness and contrast remain separate, single-responsibility modules.

    Args:
        brightness_limit: Limit range for brightness. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations RandomBrightnessContrast transform (contrast off).
    """
    return A.RandomBrightnessContrast(
        brightness_limit=brightness_limit if brightness_limit is not None else config.PIPELINE_BRIGHTNESS_LIMIT,
        contrast_limit=(0.0, 0.0),
        p=p if p is not None else 1.0,
    )
