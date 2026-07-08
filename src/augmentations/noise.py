"""
Gaussian noise augmentation module.

Simulates camera sensor noise present in real-world document photographs.
"""

import albumentations as A

from src import config


def build(
    std_range: tuple[float, float] | None = None,
    p: float | None = None,
) -> A.GaussNoise:
    """Build a Gaussian noise transform.

    Args:
        std_range: Standard deviation range. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations GaussNoise transform configured with defaults or overrides.
    """
    return A.GaussNoise(
        std_range=std_range if std_range is not None else config.PIPELINE_3_NOISE_VAR_LIMIT,
        p=p if p is not None else 1.0,
    )
