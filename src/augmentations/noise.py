"""
Gaussian noise augmentation module.

Simulates camera sensor noise present in real-world document photographs.
"""

import albumentations as A

from src import config


def build() -> A.GaussNoise:
    """Build a Gaussian noise transform.

    Returns:
        An Albumentations GaussNoise transform configured with project defaults.
    """
    return A.GaussNoise(
        std_range=config.NOISE_VAR_LIMIT,
        p=config.NOISE_PROBABILITY,
    )
