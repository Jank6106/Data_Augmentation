"""
Gradient lighting augmentation module.
Simulates uneven illumination across the image (left-right or top-bottom).
"""
import numpy as np
import albumentations as A
from src import config


class RandomLightingGradient(A.ImageOnlyTransform):
    """
    Apply a linear gradient of brightness across the image.
    Supports horizontal (left bright → right dark) or vertical (top → bottom).
    """
    def __init__(self,
                 intensity_limit=(0.1, 0.3),
                 direction_prob=(0.5, 0.5),
                 p=0.5):
        super().__init__(p=p)
        self.intensity_limit = intensity_limit
        self.direction_prob = direction_prob

    def apply(self, img, intensity=0.2, direction='horizontal', **params):
        h, w = img.shape[:2]
        # Build gradient mask
        if direction == 'horizontal':
            grad = np.linspace(1 - intensity, 1, w).reshape(1, w, 1)
        else:  # vertical
            grad = np.linspace(1 - intensity, 1, h).reshape(h, 1, 1)

        img_float = img.astype(np.float32)
        img_float = img_float * grad
        return np.clip(img_float, 0, 255).astype(np.uint8)

    def get_params(self):
        intensity = np.random.uniform(*self.intensity_limit)
        direction = 'horizontal' if np.random.rand() < self.direction_prob[0] else 'vertical'
        return {'intensity': intensity, 'direction': direction}

    def get_transform_init_args_names(self):
        return ('intensity_limit', 'direction_prob')


def build() -> RandomLightingGradient:
    """Build gradient transform with project defaults."""
    return RandomLightingGradient(
        intensity_limit=config.GRADIENT_INTENSITY,
        direction_prob=config.GRADIENT_DIRECTION,
        p=config.GRADIENT_PROBABILITY
    )
