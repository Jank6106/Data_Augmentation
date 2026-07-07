"""
CLAHE (Contrast Limited Adaptive Histogram Equalization) augmentation module.

Improves contrast in local regions of document images.
"""

import albumentations as A

from src import config


def build() -> A.CLAHE:
    """Build a CLAHE transform.

    Returns:
        An Albumentations CLAHE transform configured with project defaults.
    """
    return A.CLAHE(
        clip_limit=config.CLAHE_CLIP_LIMIT,
        tile_grid_size=config.CLAHE_TILE_GRID_SIZE,
        p=config.CLAHE_PROBABILITY,
    )
