from flask import Flask, render_template, Response, request, redirect, url_for
from muscle_checker_script import *


app = Flask(__name__, template_folder="website/pages", static_folder="website")

@app.route("/")  # The function called on "http://127.0.0.1:5000/".
def main():
	return render_template("index.html", results_dict=run('insert_calendar_text.txt'))



@app.route("/abc") # Page shows when path is "http://127.0.0.1:5000/abc".
def abc():
	results_dict = run('insert_calendar_text.txt')
	return render_template("index.html", results_dict=run('insert_calendar_text.txt'))

#rendering the HTML page which has the button
@app.route('/form', methods=['GET', 'POST'])
def index():
	print(request.method)
	if request.method == "POST":
		input = request.form.get("text_input")
		# return render_template('index.html', results_dict=run('tests/test_insert_calendar_text.txt'))
		results_dict = run_string(str(input))
	return render_template('index.html', results_dict=results_dict)
	return render_template('index.html', results_dict=run('insert_calendar_text.txt'))

#background process happening without any refreshing
@app.route('/form_background/', methods=['POST'])
def run_background():
    print ("Hello")
    return render_template('index.html', forward_message="Moving on...", results_dict=run('insert_calendar_text.txt'))