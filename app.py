"""File to run the Flask App for all of my Python projects. Run it with 'flask run --host=0.0.0.0'."""

from flask import Flask, render_template, Response, request, redirect, url_for
from muscle_checker.muscle_checker_script import *

from autogenerate_gym_calendar.autogenerate_script import *


app = Flask(__name__, template_folder="flask_website/pages", static_folder="flask_website")


@app.route("/")  # The function called on "http://127.0.0.1:5000/".
def main():
    """Run when the user goes to "http://127.0.0.1:5000/".

    Returns:
        _type_: The index.html page with results from insert_calendar_text.txt.
    """
    return render_template("index.html")


@app.route('/muscle_checker', methods=['GET', 'POST'])
def muscle_checker():
    """Render muscle_checker_index.html with the results from insert_calendar_text.txt. If the user adds text to the text_input, it will give the results from that.

    Returns:
        _type_: The muscle_checker_index.html page.
    """
    results_dict = run('muscle_checker/insert_calendar_text.txt')

    hit_muscle_groups = stringify("hit_muscle_groups", results_dict)
    missed_muscle_groups = stringify("missed_muscle_groups", results_dict)
    hit_muscles = stringify("hit_muscles", results_dict)

    if request.method == "POST":
        input = request.form.get("text_input")
        # return render_template('index.html', results_dict=run('tests/test_insert_calendar_text.txt'))
        results_dict = run_string(str(input))

        hit_muscle_groups = stringify("hit_muscle_groups", results_dict)
        missed_muscle_groups = stringify("missed_muscle_groups", results_dict)
        hit_muscles = stringify("hit_muscles", results_dict)

        return render_template('muscle_checker_index.html', results_dict=results_dict, hit_muscle_groups=hit_muscle_groups, missed_muscle_groups=missed_muscle_groups, hit_muscles=hit_muscles)
    return render_template('muscle_checker_index.html', results_dict=results_dict, hit_muscle_groups=hit_muscle_groups, missed_muscle_groups=missed_muscle_groups, hit_muscles=hit_muscles)


def stringify(index: str, dictionary: dict) -> str:
    """Attain a clean stringified list given a dictionary and index.

    Args:
        index (str): The key for the dictionary.
        dictionary (dict): The dictionary itself.

    Returns:
        str: The stringified list.
    """
    result = ""
    for item in dictionary[index]:
        result += item
        result += ", "
    if len(result) == 0:
        result = "None"
    else:
        result = result[0:len(result) - 2]

    return result


@app.route("/autogenerate_gym_calendar", methods=['GET', 'POST'])  # The function called on "http://127.0.0.1:5000/".
def autogenerate_gym_calendar():
    """Run when the user goes to "http://127.0.0.1:5000/".

    Returns:
        _type_: The calendar_index.html page.
    """

    links_dict = {'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': [], 'saturday': [], 'sunday': []}


    if request.method == "POST":


        form_dict = request.form  # Contains all of the information received by the form

        print("form_dict:")
        print(form_dict)



        weekMonday = form_dict.get("weekMonday")

        days_selected = []
        monday_selected = form_dict.get("monday")  # If not selected, it is None
        tuesday_selected = form_dict.get("tuesday")
        wednesday_selected = form_dict.get("wednesday")
        thursday_selected = form_dict.get("thursday")
        friday_selected = form_dict.get("friday")
        saturday_selected = form_dict.get("saturday")
        sunday_selected = form_dict.get("sunday")

        if monday_selected:  # Adds each not None day to days_selected (e.g. ['monday', 'wednesday', 'saturday']).
            days_selected.append("monday")
        if tuesday_selected:
            days_selected.append("tuesday")
        if wednesday_selected:
            days_selected.append("wednesday")
        if thursday_selected:
            days_selected.append("thursday")
        if friday_selected:
            days_selected.append("friday")
        if saturday_selected:
            days_selected.append("saturday")
        if sunday_selected:
            days_selected.append("sunday")

        # Adds all specific obligations into a single array.
        not_ended = True
        count = 1
        specific_obligations = []
        while not_ended:
            day = form_dict.get("day" + str(count))
            exercise = form_dict.get("exercise" + str(count))

            if day != "not_selected_day" and day != None:

                specific_obligations.append([day, exercise])

                count = count + 1
            else:
                not_ended = False



        # Collates all of the useful form data into a single dict.
        form_details = {
            "week_monday": weekMonday,
            "days_selected": days_selected,
            "gym": form_dict.get("gymSessions"),
            "runs": form_dict.get("runSessions"),
            "other": form_dict.get("otherSessions"),
            "specific_obligations": specific_obligations
        }

        print("\nform_details:")
        print(form_details)

        links_dict = run_autogenerate(form_details)

        print(links_dict)
        return render_template("calendar_index.html", links_dict=links_dict, method_post=True)

    return render_template("calendar_index.html", links_dict=links_dict, method_post=False)
