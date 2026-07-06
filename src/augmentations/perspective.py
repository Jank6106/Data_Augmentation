"""
Perspective distortion augmentation module.

Simulates the perspective shift that occurs when a document is
photographed at a slight angle rather than perfectly flat.
"""

import albumentations as A

from src import config


def build() -> A.Perspective:
    """Build a perspective distortion transform.

    Returns:
        An Albumentations Perspective transform configured with project defaults.
    """
    return A.Perspective(
        scale=config.PERSPECTIVE_SCALE,
        p=config.PERSPECTIVE_PROBABILITY,
    )
