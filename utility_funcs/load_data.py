import json
import os
from pathlib import Path

def load_data_json(file_name):
    current_file = Path(__file__).resolve()             #
    project_root = current_file.parent.parent           # this block is used to calculate path to
    file_path = project_root / 'test_data' / file_name  # folder with data for tests

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return [tuple(item.values()) for item in data]