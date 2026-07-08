"""
Motion blur augmentation module.

Simulates linear motion blur caused by camera movement during acquisition.
"""

import albumentations as A

from src import config


def build(
    blur_limit: tuple[int, int] | int | None = None,
    p: float | None = None,
) -> A.MotionBlur:
    """Build a motion blur transform.

    Args:
        blur_limit: Maximum kernel size for motion blur. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations MotionBlur transform configured with defaults or overrides.
    """
    return A.MotionBlur(
        blur_limit=blur_limit if blur_limit is not None else config.PIPELINE_3_BLUR_LIMIT,
        p=p if p is not None else 1.0,
    )
