"""
Resize augmentation module.

Ensures all output images have a consistent target size.
"""

import albumentations as A

from src import config


def build(
    height: int | None = None,
    width: int | None = None,
    p: float | None = None,
) -> A.Resize:
    """Build a resize transform.

    Args:
        height: Target height. If None, uses config default.
        width: Target width. If None, uses config default.
        p: Probability of applying the transform. If None, uses config default.

    Returns:
        An Albumentations Resize transform configured with defaults or overrides.
    """
    return A.Resize(
        height=height if height is not None else config.IMAGE_HEIGHT,
        width=width if width is not None else config.IMAGE_WIDTH,
        p=p if p is not None else config.RESIZE_PROBABILITY,
    )
