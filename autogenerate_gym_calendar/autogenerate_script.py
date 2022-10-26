"""This python script is used to generate the links required to make new calendar entries."""
import urllib.parse
import random


default_form_details = {
    'week_monday': '2022-10-10',
    'days_selected': ['monday', 'tuesday', 'friday'],
    'gym': '1', 'runs': '1', 'other': '1',
    'specific_obligations': [['wednesday', 'kayaking']]
}


def run_autogenerate(form_details: dict=default_form_details) -> dict:
    """Generates all links inside of a dict to add events to the calendar.

    Args:
        form_details (dict, optional): A dictionary containing the form details from calendar_index.html. Defaults to default_form_details.

    Returns:
        dict: The calendar event links in a dict.
    """

    monday_array = []
    tuesday_array = []
    wednesday_array = []
    thursday_array = []
    friday_array = []
    saturday_array = []
    sunday_array = []


    left = []  # Contains the number of each session type
    left.append(int(form_details["gym"]))
    left.append(int(form_details["runs"]))
    left.append(int(form_details["other"]))


    total_sessions = left[0] + left[1] # + left[2]


    print(left[2])

    # Adds each specific obligation to the relevant arrays
    for x in form_details["specific_obligations"]:

        sport = x[1]

        title_string = str(sport).capitalize() + ": 0 mins (00:00)"
        title_string = urllib.parse.quote(title_string, safe='')

        event_sections = {
            "date": convert_date(form_details["week_monday"]),  # 25/10/2022
            "title": title_string,
            "description": ""
        }

        link = create_link(event_sections)


        if x[0] == "monday":
            monday_array.append(link)
        if x[0] == "tuesday":
            tuesday_array.append(link)
        if x[0] == "wednesday":
            wednesday_array.append(link)
        if x[0] == "thursday":
            thursday_array.append(link)
        if x[0] == "friday":
            friday_array.append(link)
        if x[0] == "saturday":
            saturday_array.append(link)
        if x[0] == "sunday":
            sunday_array.append(link)



    gym_sessions = ["Cardio", "Legs", "Pull", "Push"]


    days_remaining = form_details["days_selected"]


    # For each of the sessions that are being added.
    for x in range(0, total_sessions):

        # Refills gym_sessions if it is empty
        if len(gym_sessions) < 1:
            gym_sessions = ["Cardio", "Legs", "Pull", "Push"]

        # Ensures that a number isn't picked if it is 0.
        not_allowed = True
        while not_allowed:
            chosen = random.randint(0,1)
            # print("chosen: " + str(chosen))
        
            if chosen == 0 and left[0] > 0:
                not_allowed = False
                left[0] -= 1
            if chosen == 1 and left[1] > 0:
                not_allowed = False
                left[1] -= 1
            # if chosen == 2 and left[2] > 0:
            #     not_allowed = False
            #     left[2] -= 1


        sessions = ["Gym", "Run"]


        if len(days_remaining) > 0:  # If not looped through all days
            day = days_remaining.pop()
        else:   
            days_remaining = form_details["days_selected"]


        # TODO: Change date into the right format

        date_monday = convert_date(form_details["week_monday"])
        date_string = str(date_monday) + "%2F"
        date_string = date_string + str(int(date_monday) + 1)

        if chosen == 0:  # If a gym session.
            title_string = "Gym: "+ gym_sessions.pop() + ", 0 mins (00:00)"
        else:
            title_string = str(sessions[chosen]) + ": 0 mins (00:00)"
        title_string = urllib.parse.quote(title_string, safe='')

        event_sections = {
            "date": date_string,  # 25/10/2022
            "title": title_string,
            "description": ""
        }

        # print(day)
        link = create_link(event_sections)



        if day == "monday":
            monday_array.append(link)
        if day == "tuesday":
            tuesday_array.append(link)
        if day == "wednesday":
            wednesday_array.append(link)
        if day == "thursday":
            thursday_array.append(link)
        if day == "friday":
            friday_array.append(link)
        if day == "saturday":
            saturday_array.append(link)
        if day == "sunday":
            sunday_array.append(link)

        # print(link)

    # print(left)


    # print(total_sessions)

    link_dict = {
        "monday": monday_array,
        "tuesday": tuesday_array,
        "wednesday": wednesday_array,
        "thursday": thursday_array,
        "friday": friday_array,
        "saturday": saturday_array,
        "sunday": sunday_array
        
    }

    print(form_details)

    return link_dict


def create_link(event_sections: dict) -> str:

    link_start = "https://calendar.google.com/calendar/render?action=TEMPLATE"


    link_date = f'&dates={event_sections["date"]}'

    link_description = "&details="

    link_title = f'&text={event_sections["title"]}'

    # print(link_title)

    # urllib.parse.quote('/', safe='')

    # https://calendar.google.com/calendar/render?action=TEMPLATE&dates=20221025%2F20221026&details=The%20Desc&text=The%20Title

    link_full = link_start + link_date + link_description + link_title

    return link_full



def convert_date(date: str) -> str:
    """Converts date in the format of "2022-10-10" to "20221010".

    Args:
        date (str): The date in the original format.

    Returns:
        str: The date in the new format.
    """
    date_array = date.split("-")
    return "".join(date_array)

# convert_date("2022-10-10")


print(run_autogenerate())