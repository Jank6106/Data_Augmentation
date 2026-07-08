"""
Elastic deformation augmentation module.

Simulates paper warping or scanner distortion on document images.
"""

import albumentations as A

from src import config


def build(
    alpha: float | None = None,
    sigma: float | None = None,
    p: float | None = None,
) -> A.ElasticTransform:
    """Build an elastic deformation transform.

    Args:
        alpha: Scaling factor for deformation. If None, uses config default.
        sigma: Gaussian filter parameter. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations ElasticTransform configured with defaults or overrides.
    """
    return A.ElasticTransform(
        alpha=alpha if alpha is not None else config.PIPELINE_2_ELASTIC_ALPHA,
        sigma=sigma if sigma is not None else config.PIPELINE_2_ELASTIC_SIGMA,
        border_mode=config.BORDER_MODE,
        fill=config.BORDER_VALUE,
        p=p if p is not None else 1.0,
    )
