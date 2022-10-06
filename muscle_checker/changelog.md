# muscle_checker
Last update: 2022/09/29 20:31
<br /><br />
<h2>Changelog for muscle_checker</h2>

<ol>
        <li>Created the project and README.</li>
        <li>Wrote all_muscles.json to contain all exercises.</li>
        <li>Used a JSON Validator to check the formatting.</li>
        <li>Created dataclasses for Group and Muscles.</li>
        <li>Added a function to read from all_muscles.json.</li>
        <li>Updated setup.py.</li>
        <li>Got tox working.</li>
        <ul>
                <li>Create a virtual environment - "python3 -m venv venv".</li>
                <li>Activate it - ". venv/bin/activate". You can deactivate it with "deactivate".</li>
                <li>pycodestyle "\" doesn't seem to be working. Just ignoring it.</li>
        </ul>
        <li>Creates groups and muscles dicts to store all_muscles.</li>
        <li>Wrote the read_exercises_from_text_file function.</li>
        <li>Wrote the convert_exercises_list_to_dict function.</li>
        <li>Started on find_missed_muscles.</li>
        <li>Wrote suggested_exercises function.</li>
        <li>Added a main method.</li>
        <li>Added a way to take a parameter of the calendar file location. Run the script with: "python muscle_checker.py".</li>
        <li>Added a GitLab action to learn how to do it using this <a href="https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions" target="_blank">guide</a>.</li>
        <li>Made a new .github/workflows folder to hold workflows (actions) and made a Action that runs when muscle_checker changes.</li>
        Test
</ol>
