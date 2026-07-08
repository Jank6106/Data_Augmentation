"""
Gamma correction augmentation module.

Simulates non-linear brightness shifts typical of camera sensors
and varying display/capture gamma curves.
"""

import albumentations as A

from src import config


def build(
    gamma_limit: tuple[float, float] | float | None = None,
    p: float | None = None,
) -> A.RandomGamma:
    """Build a gamma correction transform.

    Args:
        gamma_limit: Limit range for gamma. If None, uses config default.
        p: Probability of applying the transform. If None, defaults to 1.0.

    Returns:
        An Albumentations RandomGamma transform configured with defaults or overrides.
    """
    return A.RandomGamma(
        gamma_limit=gamma_limit if gamma_limit is not None else config.PIPELINE_1_GAMMA_LIMIT,
        p=p if p is not None else 1.0,
    )
