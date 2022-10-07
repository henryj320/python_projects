"""Tests for muscle_checker."""
from muscle_checker_script import *

MOCK_JSON_DATA = {
        "groups": [{ "name": "Push", "muscles": ["Pecs", "Triceps"]}],
        "muscles": [
            {"name": "Pecs", "exercises": ["Bench Press", "Incline BP"]},
            {"name": "Triceps", "exercises": ["CG Bench Press", "Close Grip Bench Press"]}
        ]
    }

def test_json_file_to_dict():
    file = "tests/test_json.json"
    result = json_file_to_dict(file)  # Runs the method.

    assert isinstance(result, dict)  # Checks that the result is a dict.
    assert len(result) > 0  # Checks that the result is not empty.
    assert result == MOCK_JSON_DATA

# test_json_file_to_dict()