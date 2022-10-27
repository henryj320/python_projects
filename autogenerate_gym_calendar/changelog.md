# autogenerate_gym_calendar
Last update: 2022/10/27 23:36
<br><br>

## Changelog for autogenerate_gym_calendar

1. Created the initial project file, updated setup.py and README.
2. Filled app.py.
3. Created a new venv:
    - Initially made it with: "python3 -m venv venv"
    - Activate it with: ". venv/bin/activate"
4. Checked that Flask runs:
    - "flask run --host=0.0.0.0"
5. Merged all flask apps into one. Run it inside of python_projects:
    - "flask run --host=0.0.0.0".
    - No VE required.
6. Wrote a calendar_index.html file to contain a form to add a week's worth of new calendar items.
7. Wrote the autogenerate_script.py.
8. Added the "Results" part of the webpage.
9. Testing and bugfixing
10. Made it so that "Add to Calendar" only shows if the day is not a rest day.