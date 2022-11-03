# muscle_checker
Last update: 2022-11-03 15:34
<br><br>

## Changelog for muscle_checker

1. Created the project and README.
2. Wrote all_muscles.json to contain all exercises.
3. Used a JSON Validator to check the formatting.
4. Created dataclasses for Group and Muscles.
5. Added a function to read from all_muscles.json.
6. Updated setup.py.
7. Got tox working.
    - Create a virtual environment - "python3 -m venv venv".
    - Activate it - ". venv/bin/activate". You can deactivate it with "deactivate".
    - pycodestyle "\" doesn't seem to be working. Just ignoring it.
8. Creates groups and muscles dicts to store all_muscles.
9. Wrote the read_exercises_from_text_file function.
10. Wrote the convert_exercises_list_to_dict function.
11. Started on find_missed_muscles.
12. Wrote suggested_exercises function.
13. Added a main method.
14. Added a way to take a parameter of the calendar file location. Run the script with: "python muscle_checker.py".
15. Added a GitLab action to learn how to do it using this <a href="https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions" target="_blank">guide</a>.
16. Made a new .github/workflows folder to hold workflows (actions) and made a Action that runs when muscle_checker changes.
17. Added linting to tox.ini. Run commands:
    - conda activate .venv/venv/activate
    - "tox" to run [testenv].
    - "tox -e lint" to run [testenv:lint].
    - "tox -e tests" to run [testenv:tests].
18. Finalised muscle_checker_action.yml. Only issue is that it doesn't fail if there are pycodestyle or pydocstyle issues.
19. Tested with a MR.
20. Cleaned up the changelog.
21. Fixed all the pycodestyle and pydocstyle errors.
22. Started the test_muscle_checker.py tests.
23. Finished all of the tests. Run then with "tox -e tests".
24. Worked on allowing several groups in one exercise list.
25. Started on the front-end app. 
    - Made app.py
    - Imports muscle_checker_script
    - Run it with " . venv/bin/activate"
    - "flask run --host=0.0.0.0"
26. Added an index.html and master.css.
27. Added content passed from python.
28. Moved the script runner into a run() method that can be used by app.py.
29. Made a web UI that prints the results with a preset location for the file.
30. Added an input form for the user to insert their workout.
31. Updated the script to take a string instead of a .txt file.
32. Fully working!
33. Removed unnecessary folders and added to .gitignore. Fixed the pycache files being added to pushes.
34. Cleaned up the README.
35. Looked into using autodocumentation (Sphinx-doc)
    - Updating the tox.ini file. "changedir = docs" creates a docs file.
    - Made a source file.
    - Made a conf.py file.
    - Starting again reading the tutorials.
36. Following the Sphinx documentation.
    - Activate the ve.
    - "pip install sphinx".
    - "sphinx-build --version".
    - "sphinx-quickstart docs" - Creates the files needed to get started - docs with build, source, make.bat and MakeFile inside. Source contains several files. make.bat and MakeFile are used for common Sphinx operations like rendering content.
    - "sphinx-build -b html docs/source/ docs/build/html" - Now have our first piece of documentation.
    - Updated index.rst.
    - Tutorial said to run "make html", but it is a .bat file so will not run.
    - "pip install furo". Already installed.
    - Made the [testenv:docs] from tox.ini.
    - Now can run it with "tox -e docs".
37. Added to "index.rst" to contain everything.
38. Played around with adding CSS.
39. Fixed linting in the pipleline. Now the GitHub runner fails if linting fails.
