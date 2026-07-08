"""
Test script to verify the 3 Woodblock Data Augmentation pipelines.
Applies Pipeline 1, Pipeline 2, and Pipeline 3 to the first image found in data/input
and saves the output images for visual verification.
"""
import os
import sys
import cv2
import numpy as np

# Add the project root to python path to allow importing src
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from src import pipeline, config

def main():
    print("=" * 60)
    print("  Testing Woodblock Data Augmentation Pipelines")
    print("=" * 60)

    # 1. Locate the input directory and find the first image
    input_dir = os.path.join(project_root, "data", "input")
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    images = [f for f in os.listdir(input_dir) if f.lower().endswith(config.SUPPORTED_EXTENSIONS)]
    if not images:
        print("No images found in data/input.")
        return

    image_name = images[0]
    image_path = os.path.join(input_dir, image_name)
    print(f"Selected test image: {image_name}")

    # Read image using numpy to support unicode/Vietnamese characters in paths on Windows
    try:
        image_bytes = np.fromfile(image_path, dtype=np.uint8)
        img = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"Error reading image: {e}")
        return

    if img is None:
        print(f"Failed to decode image from path: {image_path}")
        return

    print(f"Loaded image successfully. Shape: {img.shape}")

    # 2. Build the three pipelines
    print("\nBuilding pipelines...")
    try:
        pipe1 = pipeline.build_pipeline1()
        pipe2 = pipeline.build_pipeline2()
        pipe3 = pipeline.build_pipeline3()
        print("Pipelines built successfully!")
    except Exception as e:
        print(f"Failed to build pipelines: {e}")
        return

    # 3. Create test output folder
    test_output_dir = os.path.join(project_root, "data", "test_pipelines")
    os.makedirs(test_output_dir, exist_ok=True)
    print(f"Outputs will be saved in: {test_output_dir}")

    # 4. Apply and save augmented samples
    pipelines = {
        "pipeline1_lighting": pipe1,
        "pipeline2_warp": pipe2,
        "pipeline3_blur_noise": pipe3
    }

    for name, pipe in pipelines.items():
        print(f"\nApplying {name}...")
        try:
            # Generate 3 samples for each pipeline to verify randomness/correctness
            for i in range(3):
                augmented = pipe(image=img)
                aug_img = augmented["image"]
                
                # Check output shape
                expected_shape = (config.RESIZE_HEIGHT, config.RESIZE_WIDTH, 3) if config.RESIZE_PROBABILITY > 0 else img.shape
                if aug_img.shape != expected_shape:
                    print(f"[WARNING] Shape mismatch. Expected {expected_shape}, got {aug_img.shape}")
                
                # Save augmented image
                out_name = f"{name}_sample_{i}.png"
                out_path = os.path.join(test_output_dir, out_name)
                
                # Encode and write
                ext = os.path.splitext(out_path)[1]
                success, encoded_img = cv2.imencode(ext, aug_img)
                if success:
                    encoded_img.tofile(out_path)
                    print(f"  Saved sample {i}: {out_name}")
                else:
                    print(f"  [ERROR] Failed to save sample {i}")
        except Exception as e:
            print(f"  [ERROR] Execution failed for {name}: {e}")

    print("\nTest completed successfully!")

if __name__ == "__main__":
    main()
