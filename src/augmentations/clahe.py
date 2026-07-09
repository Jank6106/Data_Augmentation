"""
CLAHE augmentation module.

Simulates local contrast enhancement commonly caused by
image preprocessing or uneven illumination.
"""

import albumentations as A

from src import config


def build(
    clip_limit: tuple[float, float] | float | None = None,
    tile_grid_size: tuple[int, int] | None = None,
    p: float | None = None,
) -> A.CLAHE:
    """Build a CLAHE transform.

    Args:
        clip_limit:
            Contrast clipping limit.
            If None, uses config default.
        tile_grid_size:
            Size of grid for histogram equalization.
            If None, uses config default.
        p:
            Probability of applying the transform.
            If None, defaults to 1.0.

    Returns:
        An Albumentations CLAHE transform.
    """
    return A.CLAHE(
        clip_limit=clip_limit
        if clip_limit is not None
        else config.CLAHE_CLIP_LIMIT,
        tile_grid_size=tile_grid_size
        if tile_grid_size is not None
        else config.CLAHE_TILE_GRID_SIZE,
        p=p if p is not None else 1.0,
    )