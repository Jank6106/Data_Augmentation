"""
Rotation augmentation module.

Simulates slight document rotation during scanning or photography.
"""

import albumentations as A

from src import config


def build() -> A.Rotate:
    """Build a rotation transform.

    Returns:
        An Albumentations Rotate transform configured with project defaults.
    """
    return A.Rotate(
        limit=config.ROTATE_LIMIT,
        border_mode=config.ROTATE_BORDER_MODE,
        fill=config.ROTATE_BORDER_VALUE,
        p=config.ROTATE_PROBABILITY,
    )
