# CLAUDE.md

# Woodblock Data Augmentation

## Project Purpose

This project provides a modular data augmentation pipeline for OCR datasets, especially Vietnamese woodblock document images.

The project follows a modular architecture where every augmentation is implemented as an independent module. The pipeline combines these modules into a complete augmentation workflow.

The goal is to make the project:

- Easy to maintain
- Easy to extend
- Easy to test
- Easy to reuse

---

# Project Structure

```
woodblock-data-augmentation/

├── data/
│   ├── input/
│   └── output/
│
├── src/
│
│   ├── augmentations/
│   │     __init__.py
│   │     rotate.py
│   │     blur.py
│   │     brightness.py
│   │     contrast.py
│   │     gamma.py
│   │     noise.py
│   │     perspective.py
│   │     resize.py
│   │     ...
│   │
│   ├── pipeline.py
│   ├── dataset.py
│   ├── config.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# Architecture Rules

## 1. One module = One augmentation

Each augmentation must be implemented in a separate Python file.

Example:

```
rotate.py
blur.py
gamma.py
noise.py
perspective.py
```

Each module exposes exactly one public function:

```python
def build():
    ...
```

The function returns one Albumentations transform.

The module should not:

- read images
- save images
- iterate over datasets
- create pipelines

Its only responsibility is creating one augmentation.

---

## 2. pipeline.py

`pipeline.py` is responsible for combining augmentation modules.

Example:

```python
pipeline = A.Compose([
    rotate.build(),
    blur.build(),
    gamma.build(),
    noise.build(),
    resize.build(),
])
```

No augmentation implementation should exist here.

---

## 3. dataset.py

Responsibilities:

- Read images from input directory
- Apply augmentation pipeline
- Save augmented images
- Generate multiple samples per image

Do not implement augmentation logic inside this file.

---

## 4. config.py

All configurable parameters must be stored here.

Examples:

- image size
- probabilities
- rotation angle
- blur size
- gamma range
- input directory
- output directory
- output images per source image

Avoid hardcoded values in other files.

---

## 5. main.py

The entry point of the application.

Responsibilities:

- Initialize the augmentation process
- Call dataset processing

Nothing else.

---

# Coding Principles

Always follow:

- Single Responsibility Principle
- Separation of Concerns
- Reusable modules
- No duplicated code
- Clear function names
- Small functions

---

# Adding a New Augmentation

When adding a new augmentation:

1. Create a new module inside

```
src/augmentations/
```

Example

```
jpeg_compression.py
```

2. Implement

```python
def build():
    ...
```

3. Import it in

```
pipeline.py
```

Do not modify dataset.py unless dataset processing changes.

---

# OCR Guidelines

This project targets OCR datasets.

Prefer augmentations that simulate real-world document acquisition:

- slight rotation
- perspective distortion
- uneven illumination
- blur
- camera noise
- brightness variation
- contrast variation
- image compression

Avoid unrealistic augmentations.

HorizontalFlip and VerticalFlip should not be used unless explicitly requested because flipped text is not representative of real OCR data.

---

# Code Quality

Generated code should be:

- Modular
- Readable
- Extensible
- Production-ready

Avoid:

- Notebook-style scripts
- Large monolithic functions
- Hardcoded paths
- Duplicated logic

---

# AI Coding Rules

When generating code:

- Follow the existing project structure.
- Do not rewrite unrelated files.
- Reuse existing modules whenever possible.
- Keep each module focused on a single responsibility.
- Every new augmentation should be added as a new module under `src/augmentations/`.
- All public functions should include docstrings and type hints.
- Follow PEP 8 naming conventions.
- Prefer maintainability over clever implementations.
