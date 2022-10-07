# muscle_checker
Last update: 2022/10/07 12:20
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
    - "tox -e test" to run [testenv:tests].
18. Finalised muscle_checker_action.yml. Only issue is that it doesn't fail if there are pycodestyle or pydocstyle issues.
19. Tested with a MR.
20. Cleaned up the changelog.
21. Fixed all the pycodestyle and pydocstyle errors.
22. Started the test_muscle_checker.py tests.
