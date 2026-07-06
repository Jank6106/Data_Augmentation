"""
Brightness augmentation module.

Simulates uneven illumination conditions during document capture.
"""

import albumentations as A

from src import config


def build() -> A.RandomBrightnessContrast:
    """Build a brightness-only transform.

    Uses RandomBrightnessContrast with contrast disabled so that
    brightness and contrast remain separate, single-responsibility modules.

    Returns:
        An Albumentations RandomBrightnessContrast transform (contrast off).
    """
    return A.RandomBrightnessContrast(
        brightness_limit=config.BRIGHTNESS_LIMIT,
        contrast_limit=(0.0, 0.0),
        p=config.BRIGHTNESS_PROBABILITY,
    )
