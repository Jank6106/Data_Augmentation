"""
Resize augmentation module.

Ensures all output images have a consistent target size.
"""

import albumentations as A

from src import config


def build() -> A.Resize:
    """Build a resize transform.

    Returns:
        An Albumentations Resize transform configured with project defaults.
    """
    return A.Resize(
        height=config.RESIZE_HEIGHT,
        width=config.RESIZE_WIDTH,
        p=config.RESIZE_PROBABILITY,
    )
