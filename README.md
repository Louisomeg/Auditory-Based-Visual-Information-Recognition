# Auditory-Based Visual Information Recognition

This repository contains Python scripts for generating simple black-and-white patterns and displaying them sequentially in a fullscreen window. It can be used to test how auditory cues might assist recognition of basic visual stimuli.

## Components
- `generate_patterns.py` creates PNG files of various patterns and writes a `pattern_catalog.csv` describing them.
- `experiment_run.py` shows each pattern in fullscreen for a fixed duration, logging timestamps to `experiment_log.csv`.

The image files in `patterns/` and the CSV logs can be regenerated, so they are excluded in `.gitignore` to keep the repository clean.

## Usage
1. Install dependencies: `pip install pygame pillow`.
2. Run `python generate_patterns.py` to create pattern images.
3. Start the experiment with `python experiment_run.py`.

