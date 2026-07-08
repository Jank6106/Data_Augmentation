"""
Augmentation pipeline module.

Combines all individual augmentation modules into a single
Albumentations Compose pipeline. No augmentation parameters or logic
should exist in this file.
"""

import albumentations as A

from src.augmentations import (
    blur,
    brightness,
    contrast,
    elastic,
    gamma,
    gradient,
    motion_blur,
    noise,
    perspective,
    resize,
    rotate,
    salt_pepper,
)


def build_pipeline1() -> A.Compose:
    """Build Pipeline 1 (Lighting simulation):
    resize -> gamma (0.8–1.2) -> brightness (0.8–1.2) -> contrast (0.8–1.2) -> gradient.

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(),
        gamma.build(),
        brightness.build(),
        contrast.build(),
        gradient.build(),
    ])
    return pipeline


def build_pipeline2() -> A.Compose:
    """Build Pipeline 2 (Angle/Warp simulation):
    resize -> rotate (-10° to 10°) -> perspective (shift < 0.1) -> elastic (alpha 20–30, sigma 4–5).

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(),
        rotate.build(),
        perspective.build(),
        elastic.build(),
    ])
    return pipeline


def build_pipeline3() -> A.Compose:
    """Build Pipeline 3 (Blur/Noise simulation):
    resize -> motion_blur or blur (kernel <= 3x3) -> noise (var < 0.01) -> salt_pepper (prob < 0.02).

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(),
        A.OneOf([
            motion_blur.build(),
            blur.build(),
        ], p=1.0),
        noise.build(),
        salt_pepper.build(),
    ])
    return pipeline
