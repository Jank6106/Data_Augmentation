"""
Salt and pepper noise augmentation module.

Simulates dust, mold, or print defects on woodblock document images.
"""

import albumentations as A

from src import config


def build(
    amount: tuple[float, float] | None = None,
    salt_vs_pepper: tuple[float, float] | None = None,
    p: float | None = None,
) -> A.SaltAndPepper:
    """Build a Salt and Pepper noise transform.

    Args:
        amount: Fraction of pixels to replace with noise. If None, uses config default.
        salt_vs_pepper: Ratio of salt to pepper. If None, uses config default.
        p: Probability of applying the transform. If None, uses config default.

    Returns:
        An Albumentations SaltAndPepper transform configured with defaults or overrides.
    """
    return A.SaltAndPepper(
        amount=amount if amount is not None else config.SALT_PEPPER_AMOUNT,
        salt_vs_pepper=salt_vs_pepper if salt_vs_pepper is not None else config.SALT_PEPPER_VS_PEPPER,
        p=p if p is not None else config.SALT_PEPPER_PROBABILITY,
    )
