"""
Augmentation pipeline module.

Combines all individual augmentation modules into a single
Albumentations Compose pipeline.
"""

import albumentations as A

from src.augmentations import (
    blur,
    brightness,
    clahe,
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
    shadow,
)


# ===========================
# Single Augmentation
# ===========================

def build_single_pipeline() -> A.Compose:
    """Apply exactly ONE augmentation."""

    pipeline = A.Compose([
        resize.build(),
        A.OneOf([
            gamma.build(),
            brightness.build(),
            contrast.build(),
            gradient.build(),
            clahe.build(),
            shadow.build(),

            rotate.build(),
            perspective.build(),
            elastic.build(),

            motion_blur.build(),
            blur.build(),
            noise.build(),
            salt_pepper.build(),
        ], p=1.0),
    ])

    return pipeline


# ===========================
# Multiple Augmentation
# ===========================

def build_multi_pipeline() -> A.Compose:
    """Apply one complete augmentation pipeline."""

    pipeline = A.Compose([
        resize.build(),

        A.OneOf([
            # Lighting
            A.Compose([
                gamma.build(),
                brightness.build(),
                contrast.build(),
                gradient.build(),
                clahe.build(),
                shadow.build(),
            ]),

            # Geometry
            A.Compose([
                rotate.build(),
                perspective.build(),
                elastic.build(),
            ]),

            # Blur / Noise
            A.Compose([
                A.OneOf([
                    motion_blur.build(),
                    blur.build(),
                ], p=1.0),
                noise.build(),
                salt_pepper.build(),
            ]),
        ], p=1.0)
    ])

    return pipeline


# ===========================
# Final Pipeline
# ===========================

def build_pipeline() -> A.Compose:
    """
    Randomly choose between:

    - Single augmentation
    - Multiple augmentation
    """

    pipeline = A.OneOf([
        build_single_pipeline(),
        build_multi_pipeline(),
    ], p=1.0)

    return pipeline