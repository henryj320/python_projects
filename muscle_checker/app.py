"""File to run the Flask App. Run it with 'flask run --host=0.0.0.0'."""

from flask import Flask, render_template, Response, request, redirect, url_for
from muscle_checker_script import *


app = Flask(__name__, template_folder="website/pages", static_folder="website")


@app.route("/")  # The function called on "http://127.0.0.1:5000/".
def main():
    """Run when the user goes to "http://127.0.0.1:5000/".

    Returns:
        _type_: The index.html page with results from insert_calendar_text.txt.
    """
    return render_template("index.html", results_dict=run('insert_calendar_text.txt'))


@app.route('/form', methods=['GET', 'POST'])
def index():
    """Render index.html with the results from insert_calendar_text.txt. If the user adds text to the text_input, it will give the results from that.

    Returns:
        _type_: The index.html page.
    """
    if request.method == "POST":
        input = request.form.get("text_input")
        # return render_template('index.html', results_dict=run('tests/test_insert_calendar_text.txt'))
        results_dict = run_string(str(input))
        return render_template('index.html', results_dict=results_dict)
    return render_template('index.html', results_dict=run('insert_calendar_text.txt'))
