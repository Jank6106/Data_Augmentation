"""
Motion blur augmentation module.

Simulates linear motion blur caused by camera movement during acquisition.
"""

import albumentations as A

from src import config


def build() -> A.MotionBlur:
    """Build a motion blur transform.

    Returns:
        An Albumentations MotionBlur transform configured with project defaults.
    """
    return A.MotionBlur(
        blur_limit=config.MOTION_BLUR_LIMIT,
        p=config.MOTION_BLUR_PROBABILITY,
    )
