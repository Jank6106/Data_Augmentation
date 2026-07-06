"""
Gamma correction augmentation module.

Simulates non-linear brightness shifts typical of camera sensors
and varying display/capture gamma curves.
"""

import albumentations as A

from src import config


def build() -> A.RandomGamma:
    """Build a gamma correction transform.

    Returns:
        An Albumentations RandomGamma transform configured with project defaults.
    """
    return A.RandomGamma(
        gamma_limit=config.GAMMA_LIMIT,
        p=config.GAMMA_PROBABILITY,
    )
