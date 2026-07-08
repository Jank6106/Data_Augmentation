"""
Rotation augmentation module.

Simulates slight document rotation during scanning or photography.
"""

import albumentations as A

from src import config


def build(
    limit: tuple[float, float] | float | None = None,
    p: float | None = None,
) -> A.Rotate:
    """Build a rotation transform.

    Args:
        limit: Limit range for rotation. If None, uses config default.
        p: Probability of applying the transform. If None, uses config default.

    Returns:
        An Albumentations Rotate transform configured with defaults or overrides.
    """
    return A.Rotate(
        limit=limit if limit is not None else config.ROTATE_LIMIT,
        border_mode=config.ROTATE_BORDER_MODE,
        fill=config.ROTATE_BORDER_VALUE,
        p=p if p is not None else config.ROTATE_PROBABILITY,
    )
