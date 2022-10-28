"""This python script is used to generate the links required to make new calendar entries."""
from calendar import week
import urllib.parse
import random

# Default used for testing.
default_form_details = {
    'week_monday': '2022-10-10',
    'days_selected': ['monday', 'tuesday', 'friday'],
    'gym': '1', 'runs': '1', 'other': '1',
    'specific_obligations': [['wednesday', 'kayaking']]
}


def run_autogenerate(form_details: dict = default_form_details) -> dict:
    """Generate all links inside of a dict to add events to the calendar.

    Args:
        form_details (dict, optional): A dictionary containing the form details from calendar_index.html. Defaults to default_form_details.

    Returns:
        dict: The calendar event links in a dict.
    """
    # Arrays to contain all links to calendar invites.
    monday_array = []
    tuesday_array = []
    wednesday_array = []
    thursday_array = []
    friday_array = []
    saturday_array = []
    sunday_array = []

    left = []  # Contains the number of each session type.
    left.append(int(form_details["gym"]))
    left.append(int(form_details["runs"]))
    left.append(int(form_details["other"]))

    total_sessions = left[0] + left[1]  # Totals the number of sessions.

    week_dates = calculate_dates(form_details["week_monday"])  # An array of dates for each weekday in the converted format.

    # Adds each specific obligation to the relevant arrays.
    for x in form_details["specific_obligations"]:

        sport = x[1]  # E.g. "kayaking"

        title_string = str(sport).capitalize() + ": 0 mins (00:00)"
        title_string = urllib.parse.quote(title_string, safe='')

        desc_string = urllib.parse.quote("Generated by autogenerate_script.", safe='')  # Converts the description to a URL-friendly format.

        event_sections = {
            "date": week_dates[0],  # Defaults to the date of the Monday.
            "title": title_string,  # E.g. "Kayaking: 0 mins (00:00)".
            "description": desc_string
        }

        if x[0] == "monday":
            event_sections.update({"date": week_dates[0]})
            monday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "tuesday":
            event_sections.update({"date": week_dates[1]})
            tuesday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "wednesday":
            event_sections.update({"date": week_dates[2]})
            wednesday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "thursday":
            event_sections.update({"date": week_dates[3]})
            thursday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "friday":
            event_sections.update({"date": week_dates[4]})
            friday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "saturday":
            event_sections.update({"date": week_dates[5]})
            saturday_array.append([create_link(event_sections), str.capitalize(sport)])

        if x[0] == "sunday":
            event_sections.update({"date": week_dates[6]})
            sunday_array.append([create_link(event_sections), str.capitalize(sport)])

    gym_sessions = ["Cardio", "Push", "Pull", "Legs"]  # Backwards so that they can be pop() off.

    days_remaining = form_details["days_selected"]

    # For each of the sessions that are being added.
    for x in range(0, total_sessions):

        # Refills gym_sessions if it is empty
        if len(gym_sessions) < 1:
            gym_sessions = ["Cardio", "Push", "Pull", "Legs"]

        # Ensures that a number isn't picked if it is 0. E.g. no runs left.
        not_allowed = True
        while not_allowed:
            chosen = random.randint(0, 1)
            # print("chosen: " + str(chosen))

            if chosen == 0 and left[0] > 0:
                not_allowed = False
                left[0] -= 1
            if chosen == 1 and left[1] > 0:
                not_allowed = False
                left[1] -= 1

        sessions = ["Gym", "Run"]

        if len(days_remaining) > 0:  # If not looped through all days.
            day = days_remaining.pop()
        else:  # Refills the days_remaining.
            days_remaining = form_details["days_selected"]

        gym_session = gym_sessions.pop()
        session_type = ""

        if chosen == 0:  # If a gym session.
            title_string = "Gym: " + gym_session + ", 0 mins (00:00)"
            session_type = "Gym (" + gym_session + ")"
        elif chosen == 1:  # If a run.
            title_string = "Ran 0.0K in 00:00"
            session_type = "Run"
        else:
            title_string = str(sessions[chosen]) + ": 0 mins (00:00)"
            session_type = str(sessions[chosen])
        title_string = urllib.parse.quote(title_string, safe='')

        desc_string = urllib.parse.quote("Generated by autogenerate_script.", safe='')

        event_sections = {
            "date": week_dates[0],  # Defaults to the Monday.
            "title": title_string,
            "description": desc_string
        }

        if day == "monday":
            event_sections.update({"date": week_dates[0]})
            monday_array.append([create_link(event_sections), session_type])

        if day == "tuesday":
            event_sections.update({"date": week_dates[1]})
            tuesday_array.append([create_link(event_sections), session_type])

        if day == "wednesday":
            event_sections.update({"date": week_dates[2]})
            wednesday_array.append([create_link(event_sections), session_type])

        if day == "thursday":
            event_sections.update({"date": week_dates[3]})
            thursday_array.append([create_link(event_sections), session_type])

        if day == "friday":
            event_sections.update({"date": week_dates[4]})
            friday_array.append([create_link(event_sections), session_type])

        if day == "saturday":
            event_sections.update({"date": week_dates[5]})
            saturday_array.append([create_link(event_sections), session_type])

        if day == "sunday":
            event_sections.update({"date": week_dates[6]})
            sunday_array.append([create_link(event_sections), session_type])

    link_dict = {
        "monday": monday_array,
        "tuesday": tuesday_array,
        "wednesday": wednesday_array,
        "thursday": thursday_array,
        "friday": friday_array,
        "saturday": saturday_array,
        "sunday": sunday_array
    }

    for day in link_dict:
        if link_dict[day] == []:
            link_dict[day] = [["-", "Rest"]]

    return link_dict


def create_link(event_sections: dict) -> str:
    """Given the event_section, creates the Goolge calendar link and returns it.

    Args:
        event_sections (dict): A dict containing the title, description and date of the event.

    Returns:
        str: The URL to the Google calendar event.
    """
    link_start = "https://calendar.google.com/calendar/render?action=TEMPLATE"

    dates = int(event_sections["date"])
    dated = str(dates) + "/" + str(dates + 1)
    link_date = f'&dates={dated}'

    link_description = f'&details={event_sections["description"]}'

    link_title = f'&text={event_sections["title"]}'

    # https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20221025%2F20221026&details=The%20Desc&text=The%20Title
    link_full = link_start + link_date + link_description + link_title

    return link_full


def convert_date(date: str) -> str:
    """Convert date in the format of "2022-10-10" to "20221010".

    Args:
        date (str): The date in the original format.

    Returns:
        str: The date in the new format.
    """
    date_array = date.split("-")
    return "".join(date_array)


def calculate_dates(week_monday: str) -> list:
    """Convert the date from "2022-10-25" to "20221025" and makes sure that the day is in the correct month.

    Args:
        week_monday (str): The monday of the week.

    Returns:
        list: An array of all the dates converted.
    """
    week_monday_array = week_monday.split("-")  # Splits "2022-10-25" into ["2022", "10", "25"].
    year = week_monday_array[0]
    month = week_monday_array[1]
    day = week_monday_array[2]

    week_dates = [convert_date(week_monday)]  # Contains Monday.

    total_days = 31
    thirty_days = [4, 6, 9, 11]  # The dates with 30 days (i.e. April, June, etc)

    if month == 2:  # If the month is february.
        if int(year) % 4 == 0:  # If a leap year.
            total_days = 29
        else:
            total_days = 28

    elif month in thirty_days:  # If in a month with 30 days.
        total_days = 30

    for x in range(1, 7):  # 1, 2, 3, 4, 5, 6
        next_day = int(day) + x
        use_month = month

        if next_day > total_days:  # If it goes over the number of days in the month (e.g. 32)
            next_day = "0" + str(next_day - total_days)
            use_month = str(int(month) + 1)

        week_dates.append(str(year) + str(use_month) + str(next_day))

    return week_dates


print(run_autogenerate())
