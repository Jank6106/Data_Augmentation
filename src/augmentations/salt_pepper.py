"""
Salt and pepper noise augmentation module.

Simulates dust, mold, or print defects on woodblock document images.
"""

import albumentations as A

from src import config


def build() -> A.SaltAndPepper:
    """Build a Salt and Pepper noise transform.

    Returns:
        An Albumentations SaltAndPepper transform configured with project defaults.
    """
    return A.SaltAndPepper(
        amount=config.SALT_PEPPER_AMOUNT,
        salt_vs_pepper=config.SALT_PEPPER_VS_PEPPER,
        p=config.SALT_PEPPER_PROBABILITY,
    )
