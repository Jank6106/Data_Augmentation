"""
Perspective distortion augmentation module.

Simulates the perspective shift that occurs when a document is
photographed at a slight angle rather than perfectly flat.
"""

import albumentations as A

from src import config


def build(
    scale: tuple[float, float] | float | None = None,
    p: float | None = None,
) -> A.Perspective:
    """Build a perspective distortion transform.

    Args:
        scale: Limit range for perspective shift. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations Perspective transform configured with defaults or overrides.
    """
    return A.Perspective(
        scale=scale if scale is not None else config.PIPELINE_PERSPECTIVE_SCALE,
        p=p if p is not None else 1.0,
    )
