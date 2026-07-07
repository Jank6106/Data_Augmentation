"""
Elastic deformation augmentation module.

Simulates paper warping or scanner distortion on document images.
"""

import albumentations as A

from src import config


def build() -> A.ElasticTransform:
    """Build an elastic deformation transform.

    Returns:
        An Albumentations ElasticTransform configured with project defaults.
    """
    return A.ElasticTransform(
        alpha=config.ELASTIC_ALPHA,
        sigma=config.ELASTIC_SIGMA,
        border_mode=config.ELASTIC_BORDER_MODE,
        fill=config.ELASTIC_BORDER_VALUE,
        p=config.ELASTIC_PROBABILITY,
    )
