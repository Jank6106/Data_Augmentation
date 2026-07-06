"""
Augmentation pipeline module.

Combines all individual augmentation modules into a single
Albumentations Compose pipeline. No augmentation implementation
should exist in this file.
"""

import albumentations as A

from src.augmentations import (
    blur,
    brightness,
    contrast,
    gamma,
    noise,
    perspective,
    resize,
    rotate,
)


def build() -> A.Compose:
    """Build the complete augmentation pipeline.

    Returns:
        An Albumentations Compose pipeline combining all augmentation modules.
    """
    pipeline = A.Compose([
        rotate.build(),
        perspective.build(),
        blur.build(),
        brightness.build(),
        contrast.build(),
        gamma.build(),
        noise.build(),
        resize.build(),
    ])
    return pipeline
