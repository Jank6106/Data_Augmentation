"""
Entry point for the Woodblock Data Augmentation application.

Responsibilities:
- Initialize the augmentation pipeline.
- Trigger dataset processing.
"""

from src import pipeline, dataset


def main() -> None:
    """Run the full augmentation workflow."""
    print("=" * 60)
    print("  Woodblock Data Augmentation Pipeline")
    print("=" * 60)

    aug_pipeline = pipeline.build()
    total = dataset.process(aug_pipeline)

    print(f"\nDone. {total} augmented images saved.")


if __name__ == "__main__":
    main()
