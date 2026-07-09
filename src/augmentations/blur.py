"""
Blur augmentation module.

Simulates camera defocus or motion blur on document images.
"""

import albumentations as A

from src import config


def build(
    blur_limit: tuple[int, int] | int | None = None,
    p: float | None = None,
) -> A.Blur:
    """Build a blur transform.

    Args:
        blur_limit: Maximum kernel size for blurring. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations Blur transform configured with defaults or overrides.
    """
    return A.Blur(
        blur_limit=blur_limit if blur_limit is not None else config.PIPELINE_BLUR_LIMIT,
        p=p if p is not None else 1.0,
    )
