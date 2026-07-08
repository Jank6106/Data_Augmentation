"""
Dataset processing module.

Responsibilities:
- Read images from the input directory.
- Apply the augmentation pipeline.
- Save augmented images to the output directory.
- Generate multiple samples per source image.

No augmentation logic should be implemented in this file.
"""

import os
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

import albumentations as A

from src import config


def _collect_image_paths(input_dir: str) -> list[str]:
    """Collect all supported image file paths from the input directory.

    Args:
        input_dir: Path to the directory containing source images.

    Returns:
        A sorted list of absolute paths to image files.
    """
    paths: list[str] = []
    for entry in sorted(os.listdir(input_dir)):
        if entry.lower().endswith(config.SUPPORTED_EXTENSIONS):
            paths.append(os.path.join(input_dir, entry))
    return paths


def _read_image(path: str) -> np.ndarray:
    """Read an image from disk as a BGR NumPy array.

    Args:
        path: Absolute path to the image file.

    Returns:
        The image as a NumPy array in BGR colour space.

    Raises:
        FileNotFoundError: If the image cannot be loaded.
    """
    # Use numpy to read file bytes to support Unicode/Vietnamese characters in the path
    try:
        image_bytes = np.fromfile(path, dtype=np.uint8)
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    except Exception:
        image = None
        
    if image is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return image


def _save_image(image: np.ndarray, output_path: str) -> None:
    """Save an image to disk.

    Args:
        image: The image as a NumPy array (BGR).
        output_path: Destination file path.
    """
    # Use cv2.imencode and numpy tofile to support Unicode/Vietnamese characters in the path
    ext = os.path.splitext(output_path)[1]
    success, encoded_img = cv2.imencode(ext, image)
    if success:
        encoded_img.tofile(output_path)
    else:
        cv2.imwrite(output_path, image)


def _build_output_filename(
    source_name: str,
    sample_index: int,
) -> str:
    """Build the output filename for an augmented sample.

    Args:
        source_name: The original image filename (without extension).
        sample_index: The zero-based index of this augmented sample.

    Returns:
        A filename string like ``original_aug_003.png``.
    """
    return f"{source_name}_aug_{sample_index:03d}.png"


def process(pipelines: dict[str, A.Compose]) -> int:
    """Run the augmentation pipelines on every image in the input directory.

    For each source image, samples are generated using all provided pipelines,
    controlled by configuration variables like ``config.PIPELINE_1_SAMPLES``, etc.

    Args:
        pipelines: Dictionary mapping pipeline names (e.g. "pipeline1") to
            Albumentations Compose pipelines.

    Returns:
        The total number of augmented images saved.
    """
    input_dir: str = config.INPUT_DIR
    output_dir: str = config.OUTPUT_DIR

    os.makedirs(output_dir, exist_ok=True)

    image_paths: list[str] = _collect_image_paths(input_dir)

    if not image_paths:
        print(f"[WARNING] No images found in: {Path(input_dir).name}")
        return 0

    total_saved: int = 0

    for path in tqdm(image_paths, desc="Processing images"):
        image: np.ndarray = _read_image(path)
        source_name: str = Path(path).stem
        
        # Create a dedicated folder for each image's augmented copies
        image_output_dir = os.path.join(output_dir, f"{source_name}_aug")
        os.makedirs(image_output_dir, exist_ok=True)

        sample_index = 0
        for pipe_key, pipe in pipelines.items():
            num_samples = getattr(config, f"{pipe_key.upper()}_SAMPLES", 0)
            for _ in range(num_samples):
                augmented = pipe(image=image)
                augmented_image = augmented["image"]

                filename = _build_output_filename(source_name, sample_index)
                output_path = os.path.join(image_output_dir, filename)

                _save_image(augmented_image, output_path)
                sample_index += 1
                total_saved += 1

    return total_saved
