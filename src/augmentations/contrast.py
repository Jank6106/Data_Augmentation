"""
Contrast augmentation module.

Simulates contrast variation in scanned or photographed documents.
"""

import albumentations as A

from src import config


def build() -> A.RandomBrightnessContrast:
    """Build a contrast-only transform.

    Uses RandomBrightnessContrast with brightness disabled so that
    brightness and contrast remain separate, single-responsibility modules.

    Returns:
        An Albumentations RandomBrightnessContrast transform (brightness off).
    """
    return A.RandomBrightnessContrast(
        brightness_limit=(0.0, 0.0),
        contrast_limit=config.CONTRAST_LIMIT,
        p=config.CONTRAST_PROBABILITY,
    )
