"""
Parameter sweep for augmentation tuning.

Generate images using different parameter values so they
can be visually inspected.
"""

from pathlib import Path

import cv2
import numpy as np

from src import config
from src.dataset import _collect_image_paths, _read_image, _save_image
from src.augmentations import resize, rotate
import albumentations as A


ROTATE_VALUES = [3, 5, 8, 10, 15]


def build_pipeline(angle: int):

    return A.Compose([
        resize.build(),
        rotate.build(limit=angle),
    ])


def main():

    image_paths = _collect_image_paths(config.INPUT_DIR)

    output_root = Path(config.OUTPUT_DIR) / "parameter_sweep"

    output_root.mkdir(parents=True, exist_ok=True)

    for angle in ROTATE_VALUES:

        pipeline = build_pipeline(angle)

        save_dir = output_root / f"rotate_{angle}"
        save_dir.mkdir(exist_ok=True)

        for path in image_paths:

            image = _read_image(path)

            augmented = pipeline(image=image)["image"]

            output_path = save_dir / Path(path).name

            _save_image(
                augmented,
                str(output_path),
            )

    print("Done.")


if __name__ == "__main__":
    main()