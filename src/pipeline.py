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
    elastic,
    gamma,
    motion_blur,
    noise,
    perspective,
    resize,
    rotate,
    salt_pepper,
    gradient
)
from src import config


def build_pipeline1() -> A.Compose:
    """Build Pipeline 1 (Lighting simulation):
    resize -> gamma (0.8–1.2) -> brightness (0.8–1.2) -> contrast (0.8–1.2).

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(p=config.RESIZE_PROBABILITY),
        gamma.build(gamma_limit=config.PIPELINE_1_GAMMA_LIMIT, p=1.0),
        brightness.build(brightness_limit=config.PIPELINE_1_BRIGHTNESS_LIMIT, p=1.0),
        contrast.build(contrast_limit=config.PIPELINE_1_CONTRAST_LIMIT, p=1.0),
        gradient.build(
            intensity_limit=config.PIPELINE_1_GRADIENT_INTENSITY,
            direction_prob=config.PIPELINE_1_GRADIENT_DIRECTION,
            p=1.0
        )
    ])
    return pipeline


def build_pipeline2() -> A.Compose:
    """Build Pipeline 2 (Angle/Warp simulation):
    resize -> rotate (-10° to 10°) -> perspective (shift < 0.1) -> elastic (alpha 20–30, sigma 4–5).

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(p=config.RESIZE_PROBABILITY),
        rotate.build(limit=config.PIPELINE_2_ROTATE_LIMIT, p=1.0),
        perspective.build(scale=config.PIPELINE_2_PERSPECTIVE_SCALE, p=1.0),
        elastic.build(alpha=config.PIPELINE_2_ELASTIC_ALPHA, sigma=config.PIPELINE_2_ELASTIC_SIGMA, p=1.0),
    ])
    return pipeline


def build_pipeline3() -> A.Compose:
    """Build Pipeline 3 (Blur/Noise simulation):
    resize -> motion_blur or blur (kernel <= 3x3) -> noise (var < 0.01) -> salt_pepper (prob < 0.02).

    Returns:
        An Albumentations Compose pipeline.
    """
    pipeline = A.Compose([
        resize.build(p=config.RESIZE_PROBABILITY),
        A.OneOf([
            motion_blur.build(blur_limit=config.PIPELINE_3_BLUR_LIMIT, p=1.0),
            blur.build(blur_limit=config.PIPELINE_3_BLUR_LIMIT, p=1.0),
        ], p=1.0),
        noise.build(std_range=config.PIPELINE_3_NOISE_VAR_LIMIT, p=1.0),
        salt_pepper.build(amount=config.PIPELINE_3_SALT_PEPPER_AMOUNT, p=1.0),
    ])
    return pipeline
