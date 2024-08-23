#!/bin/bash

FILE_PATH="28_task/8.py"

python -m black "$FILE_PATH"
python -m darker "$FILE_PATH"
python -m ruff check --fix "$FILE_PATH"
python -m mypy "$FILE_PATH"