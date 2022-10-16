"""File to run the Flask App for all of my Python projects. Run it with 'flask run --host=0.0.0.0'."""

from flask import Flask, render_template, Response, request, redirect, url_for
from muscle_checker.muscle_checker_script import *


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


@app.route("/autogenerate_gym_calendar")  # The function called on "http://127.0.0.1:5000/".
def autogenerate_gym_calendar():
    """Run when the user goes to "http://127.0.0.1:5000/".

    Returns:
        _type_: The calendar_index.html page.
    """
    return render_template("calendar_index.html")
