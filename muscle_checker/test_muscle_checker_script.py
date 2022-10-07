"""Tests for muscle_checker."""
from muscle_checker_script import *

MOCK_JSON_DATA = {
    'groups': [
        {'name': 'Push', 'muscles': ['Pecs', 'Triceps', 'Front Deltoids']},
        {'name': 'Legs', 'muscles': ['Glutes', 'Quads', 'Hamstrings', 'Calves']}
    ],
    'muscles': [
        {'name': 'Pecs', 'exercises': ['Bench Press', 'Incline BP']},
        {'name': 'Triceps', 'exercises': ['Tricep Pull-Downs', 'Close Grip Bench Press']},
        {'name': 'Front Deltoids', 'exercises': ['Front Shoulder Raises']},
        {'name': 'Quads', 'exercises': ['Squats', 'Leg Press']}
    ]
}

MOCK_CALENDAR_LIST = ['Bench Press', 'Tricep Pull-Downs', 'Leg Press']

MOCK_HIT_MUSCLES = [
    {'name': 'Pecs', 'exercises': ['Bench Press']},
    {'name': 'Triceps', 'exercises': ['Tricep Pull-Downs']},
    {'name': 'Quads', 'exercises': ['Leg Press']}
]


def test_json_file_to_dict():
    """Test method for muscle_checker_script.json_file_to_dict()."""
    file = "tests/test_json.json"
    result = json_file_to_dict(file)  # Runs the method.

    assert isinstance(result, dict)  # Checks that the result is a dict.
    assert len(result) > 0  # Checks that the result is not empty.
    assert result == MOCK_JSON_DATA


def test_read_exercises_from_text_file():
    """Test method for muscle_checker_script.read_exercises_from_text_file()."""
    file = "tests/test_insert_calendar_text.txt"
    result = read_exercises_from_text_file(file)

    assert isinstance(result, list)
    assert len(result) > 0  # Checks that the result is not empty.
    assert result == MOCK_CALENDAR_LIST  # Checks that all exercises are grabbed.
    assert len(result) == 3  # Chceks that all exercises were added.


def test_convert_exercises_list_to_dict():
    """Test method for muscle_checker_script.convert_exercises_list_to_dict()."""
    all_muscles = json_file_to_dict("tests/test_json.json")
    all_groups = all_muscles["groups"]
    all_muscles = all_muscles["muscles"]

    result = convert_exercises_list_to_dict(1, all_groups, all_muscles, MOCK_CALENDAR_LIST)
    assert isinstance(result, dict)  # Checks that the result is a dict.
    assert len(result["muscles"]) == 3  # Checks that all 3 muscles are picked up (Pecs, Triceps, Quads).
    assert result["groups"] == ["Push", "Legs"]  # Checks the group has automatically been picked up as "Push"
    assert len(result) == 3  # Checks that result contains "session_number", "group" and "muscles"


def test_find_missed_muscles():
    """Test method for muscle_checker_script.find_missed_muscles()."""
    groups = ["Push", "Legs"]
    all_muscles = json_file_to_dict("tests/test_json.json")
    all_groups = all_muscles["groups"]

    result = find_missed_muscles(groups, MOCK_HIT_MUSCLES, all_groups)

    assert isinstance(result, list)  # Checks that the result is a list.
    assert result == ["Front Deltoids", "Glutes", "Hamstrings", "Calves"]  # Checks that the result only contains "Front Deltoids".


def test_suggested_exercises():
    """Test method for muscle_checker_script.suggested_exercises()."""
    all_muscles = json_file_to_dict("tests/test_json.json")
    all_muscles = all_muscles["muscles"]
    missed_muscle = "Front Deltoids"

    result = suggested_exercises(all_muscles, missed_muscle)

    assert result == "You didn't train your Front Deltoids.\nTo train this, you could perform or Front Shoulder Raises.\n"


# This block makes it so that you can run the tests with "python3 test_muscle_checker_script.py".
test_json_file_to_dict()
test_read_exercises_from_text_file()
test_convert_exercises_list_to_dict()
test_find_missed_muscles()
test_suggested_exercises()
