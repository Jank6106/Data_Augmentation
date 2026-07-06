"""
Blur augmentation module.

Simulates camera defocus or motion blur on document images.
"""

import albumentations as A

from src import config


def build() -> A.Blur:
    """Build a blur transform.

    Returns:
        An Albumentations Blur transform configured with project defaults.
    """
    return A.Blur(
        blur_limit=config.BLUR_LIMIT,
        p=config.BLUR_PROBABILITY,
    )
