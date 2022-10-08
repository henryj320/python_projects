from pydoc import render_doc
from flask import Flask, render_template
from muscle_checker_script import *


app = Flask(__name__, template_folder="website/pages", static_folder="website")

@app.route("/")  # The function called on "http://127.0.0.1:5000/".
def hello_world():
	return json_file_to_dict('all_muscles.json')
	return "Hi"


@app.route("/abc") # Page shows when path is "http://127.0.0.1:5000/abc".
def abc():
	return render_template("index.html", details=json_file_to_dict('all_muscles.json'))