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

    pipelines = {
        "pipeline_1": pipeline.build_pipeline1(),
        "pipeline_2": pipeline.build_pipeline2(),
        "pipeline_3": pipeline.build_pipeline3(),
    }
    total = dataset.process(pipelines)

    print(f"\nDone. {total} augmented images saved.")


if __name__ == "__main__":
    main()
