"""Tests for autogenerate_gym_calendar."""
import urllib.parse
from autogenerate_script import *



def test_run_autogenerate():
    """Test method for autogenerate_script.run_autogenerate()."""

    # How does it react if inputs are correct?

    # How does it react if form_details is blank?

    # How does it react if event_sections contains the wrong keys?

    # Does it return a dict

    assert True

def test_create_link():
    """Test method for autogenerate_script.create_link()."""

    possible_event_sections = []

    valid_event_sections = {
            "date": "20221107",  # Monday 7th November 2022.
            "title": urllib.parse.quote("This is a title", safe=''),
            "description": urllib.parse.quote("This is a description", safe='')
    }
    possible_event_sections.append(valid_event_sections)

    no_desc_event_sections = {
        "date": "20221107",  # Monday 7th November 2022.
        "title": urllib.parse.quote("This is a title", safe=''),
        "description": ""
    }
    possible_event_sections.append(no_desc_event_sections)

    no_title_event_sections = {
        "date": "20221107",  # Monday 7th November 2022.
        # "title": urllib.parse.quote("This is a title", safe=''),
        "description": urllib.parse.quote("This is a description", safe='')
    }
    possible_event_sections.append(no_title_event_sections)

    # Contains each part of the expected output in separate array items.
    expected_output = []
    expected_output.append("https://calendar.google.com/calendar/render?action=TEMPLATE&")
    expected_output.append("dates=" + possible_event_sections[0]["date"] + "/" + str(int(possible_event_sections[0]["date"]) + 1))
    expected_output.append("&details=" + possible_event_sections[0]["description"])
    expected_output.append("&text=" + possible_event_sections[0]["title"])

    assert create_link(possible_event_sections[0]) == expected_output[0] + expected_output[1] + expected_output[2] + expected_output[3]
    assert isinstance(create_link(possible_event_sections[0]), str)
    assert create_link(possible_event_sections[1]) == expected_output[0] + expected_output[1] + expected_output[3]
    assert create_link(possible_event_sections[2]) == expected_output[0] + expected_output[1] + expected_output[2] + "&text=Title"


def test_convert_date():
    """Test method for autogenerate_script.convert_date()."""

    valid_date = "2022-11-07"

    assert convert_date(valid_date) == "20221107"
    assert convert_date("07-11-2022") == "20221107"
    assert isinstance(convert_date(valid_date), str)


def test_calculate_dates():
    """Test method for autogenerate_script.calculate_dates()."""

    # How does it react if week_monday is correct?

    # How does it react if week_monday is not a Monday?

    # How does it react if week_monday is gte 32 or lte 0?

    # Does it output a list?

    # Does it work on leap year Februaries?

    assert True

print("\n---\n\n")
#test_run_autogenerate()
# test_create_link()
# test_convert_date()
#test_calculate_dates()
