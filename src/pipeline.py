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
    gradient,
    noise,
    perspective,
    resize,
    rotate,
)


def build_pipeline1() -> A.Compose:
    """Build the main augmentation pipeline (excluding gradient).

    Returns:
        An Albumentations Compose pipeline.
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


def build_pipeline2() -> A.Compose:
    """Build the second augmentation pipeline containing only the gradient module.

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        gradient.build(),
        resize.build(),
    ])
    return pipeline
