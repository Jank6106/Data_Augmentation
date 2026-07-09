"""
Shadow augmentation module.

Simulates shadows caused by uneven lighting during
image acquisition.
"""

import albumentations as A

from src import config


def build(
    shadow_roi: tuple[float, float, float, float] | None = None,
    num_shadows_limit: tuple[int, int] | None = None,
    shadow_dimension: int | None = None,
    p: float | None = None,
) -> A.RandomShadow:
    """Build a random shadow transform.

    Args:
        shadow_roi:
            Region where shadows may appear.
            If None, uses config default.
        num_shadows_limit:
            Number of generated shadows.
            If None, uses config default.
        shadow_dimension:
            Number of vertices defining each shadow.
            If None, uses config default.
        p:
            Probability of applying the transform.
            If None, defaults to 1.0.

    Returns:
        An Albumentations RandomShadow transform.
    """
    return A.RandomShadow(
        shadow_roi=shadow_roi
        if shadow_roi is not None
        else config.SHADOW_ROI,
        num_shadows_limit=num_shadows_limit
        if num_shadows_limit is not None
        else config.SHADOW_NUM_LIMIT,
        shadow_dimension=shadow_dimension
        if shadow_dimension is not None
        else config.SHADOW_DIMENSION,
        p=p if p is not None else 1.0,
    )