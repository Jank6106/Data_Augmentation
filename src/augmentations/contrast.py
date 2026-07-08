"""
Contrast augmentation module.

Simulates contrast variation in scanned or photographed documents.
"""

import albumentations as A

from src import config


def build(
    contrast_limit: tuple[float, float] | float | None = None,
    p: float | None = None,
) -> A.RandomBrightnessContrast:
    """Build a contrast-only transform.

    Uses RandomBrightnessContrast with brightness disabled so that
    brightness and contrast remain separate, single-responsibility modules.

    Args:
        contrast_limit: Limit range for contrast. If None, uses config default.
        p: Probability of applying the transform. If None, uses config default.

    Returns:
        An Albumentations RandomBrightnessContrast transform (brightness off).
    """
    return A.RandomBrightnessContrast(
        brightness_limit=(0.0, 0.0),
        contrast_limit=contrast_limit if contrast_limit is not None else config.CONTRAST_LIMIT,
        p=p if p is not None else config.CONTRAST_PROBABILITY,
    )
