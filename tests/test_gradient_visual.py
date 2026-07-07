"""
Test script for testing the RandomLightingGradient augmentation.
Loads the first image in data/input, applies horizontal and vertical gradients,
and saves a side-by-side comparison image in data/test_gradient/.
"""
import os
import sys
import cv2
import numpy as np

# Add the project root to python path to allow importing src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.augmentations.gradient import RandomLightingGradient

def main():
    # Find the first image in data/input
    # Since we run this, paths should be relative to the workspace root
    # or constructed relative to this file's parent directory.
    # Let's make it relative to the workspace root first, but fallback to file-relative path.
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_dir = os.path.join(project_root, "data", "input")
    
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    images = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'))]
    if not images:
        print("No images found in data/input.")
        return

    # Choose the first image
    image_name = images[0]
    image_path = os.path.join(input_dir, image_name)
    
    # Read the image supporting Unicode characters in path
    try:
        image_bytes = np.fromfile(image_path, dtype=np.uint8)
        img = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"Error reading image: {e}")
        return
        
    if img is None:
        print(f"Cannot read image: {image_path}")
        return

    print(f"Loaded image: '{image_name}' with shape {img.shape}")
    
    # Create test output directory
    output_dir = os.path.join(project_root, "data", "test_gradient")
    os.makedirs(output_dir, exist_ok=True)
    
    # Apply Horizontal Gradient (intensity limit 0.4 - 1.0 for visible effect)
    grad_h = RandomLightingGradient(intensity_limit=(0.4, 1.0), direction_prob=(1.0, 0.0), p=1.0)
    img_h = grad_h(image=img)["image"]
    
    # Apply Vertical Gradient
    grad_v = RandomLightingGradient(intensity_limit=(0.4, 1.0), direction_prob=(0.0, 1.0), p=1.0)
    img_v = grad_v(image=img)["image"]
    
    # Create side-by-side comparison
    # Resize images to fit easily if they are too big
    h, w = img.shape[:2]
    max_size = 600
    if h > max_size or w > max_size:
        scale = max_size / max(h, w)
        img_resized = cv2.resize(img, (int(w * scale), int(h * scale)))
        img_h_resized = cv2.resize(img_h, (int(w * scale), int(h * scale)))
        img_v_resized = cv2.resize(img_v, (int(w * scale), int(h * scale)))
    else:
        img_resized = img
        img_h_resized = img_h
        img_v_resized = img_v
        
    # Concatenate horizontally
    comparison = np.hstack((img_resized, img_h_resized, img_v_resized))
    
    # Add text labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    h_r, w_r = img_resized.shape[:2]
    # Red text labels on top-left of each panel
    cv2.putText(comparison, "Original", (10, 40), font, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(comparison, "Horizontal Grad", (w_r + 10, 40), font, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(comparison, "Vertical Grad", (2 * w_r + 10, 40), font, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
    
    output_path = os.path.join(output_dir, f"comparison_{image_name}")
    ext = os.path.splitext(output_path)[1]
    success, encoded_img = cv2.imencode(ext, comparison)
    if success:
        encoded_img.tofile(output_path)
        print(f"Saved comparison to: {output_path}")
        print("Test completed successfully!")
    else:
        print("Failed to encode/save comparison image.")

if __name__ == "__main__":
    main()
