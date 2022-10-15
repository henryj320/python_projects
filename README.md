# **python_projects**
Last update: 2022-10-15 01:37

<br>
Make sure to update the Projects table: [All Projects Table](https://github.com/users/henryj320/projects/5)
<br><br>

## Future Project Ideas

---
<br>


## **watt_checker**<br>
**Language**: Python / Powershell<br>
**Overview**: Records the Watts-used by the laptop every 30 minutes. Record the value into an Excel spreadsheet so that a chart can be automatically generated or updated every day. Alternatively, use Python so that matplotlib and seaborn can be used. On brief research, it is not easy to grab the current power draw of a computer. Intel has some built-in, but may be complicated.<br><br>


## **weekly_goals_GUI**<br>
**Language**: Python<br>
**Overview**: Shows a progress bar for your weekly goals. For example, a progress bar on how close to your reading goal you are. You could also autorun this on startup and set your background to the progress bars by screenshotting and setting as the wallpaper. It could also show how much of your 7.5 * 5 hrs of work you've done so far. You could run this via Flask. This would make it so that you can use Python (storing values in .txt files) and a clean webpage with Bootstrap. Alternatively, you could use React for clean elements and running.<br><br>


## **wifi_users_tracker**<br>
**Language**: Linux Script<br>
**Overview**: A software which states when a new device joins your WiFi network via a notification. It could be extended to show when a device disconnects. Previous implementation of this used a for loop to read the nmap's "x devices found" string.<br><br>


## **transcripter**<br>
**Language**: Python<br>
**Overview**: Learn how to make a transcripter that converts speech to text. Look into any existing libraries that allow for this.<br><br>


## **internet_stability_recorder**<br>
**Language**: Python<br>
**Overview**: Sends a ping every 5 minutes and records the result to Excel. Use the results to automatically plot into a chart. This would show how stable the internet is throughout the day.<br><br>


## **centre_country_shower**<br>
**Language**: Python<br>
**Overview**: Shows the centre of a given country based on different factors: geological, average age, population, etc. This would show age densities, etc.<br><br>


## **running_route_generator**<br>
**Language**: Python<br>
**Overview**: The user provides a location. The script generates a path to coordinates x metres away and adds this as a route on Google Maps and outputs this to the user. This allows the user to run to a random place every time the exact distance away that they want.<br><br>


## **tcp_message_sender_and_receiver**<br>
**Language**: Python<br>
**Overview**: Write a program that sends and receives message from the basics. Generate a TCP segment with all of the fields in binary. Set up a port to send on and a port to receive on. Use your Java code as a reference. Importantly, the receiver needs to be listening on the port. Use datasubs to find how to run an app on a certain portand listen to requests. Set out the plan logically.<br><br>


## **height_determination_software**<br>
**Language**: Not a clue<br>
**Overview**: Use vanishing points to determine the height of individuals or objects inside photos. (Fspy)<br><br>


## **blender_addon_forensic_tool**<br>
**Language**: Python <br>
**Overview**: Creating simulations, blah, blah, blah.<br><br>


## **computer_writing_tool**<br>
**Language**: Not a clue<br>
**Overview**: Piece of software that analyses text, categorises words into groups (verbs, nouns, prepositions, etc.) and uses preset knowledge on sentence structures to write sentences/more.<br><br>


## **dnd_map_precedural_gen_tool**<br>
**Language**: Not a clue <br>
**Overview**: Precedurally generates tools in different settings for use by DMs and GMs in TTRPG campaigns. Different settings can be changed to tweak results. <br><br>


## **text_to_music**<br>
**Language**: not a clue <br>
**Overview**: Converts text to music based on a formula. Including tone reading through negativity/positivity of words in sentence, (minor/major). https://www.youtube.com/watch?v=PVT6WpOyf0s&feature=youtu.be<br><br>


## **precedurally_generated_evolution_of_civilisation**<br>
**Language**: Not a clue<br>
**Overview**: Tweak parameters as the civilisation and planet evolves to create stats and planet image.<br><br>


## **dnd_fun_tool**<br>
**Language**: Not a clue <br>
**Overview**: Keep track of characters, better combat system, better image display system, better tools for DM.<br><br>


## **Free_Worlds_website**<br>
**Language**: HTML/Javascript<br>
**Overview**: website go brr.<br><br>


## **full_system_search**<br>
**Language**: Python<br>
**Overview**: Similar to DocumentSystem to Git. Make a program that takes a searchterm and searches the entire computer for any documents named or containing the term. Make it show sections at a time with a progress bar to learn Python progress bars in the terminal. Add a parameter for OS so that OS files can be ignored. Output should be something like "Found: X occurrences of "example" in Documents, Y occurences of "example" in Pictures.<br><br>


## **react_dashboard**<br>
**Language**: React<br>
**Overview**: Develop a React frontend using a [template](https://www.creative-tim.com/templates/react-free). Develop it from scratch making use of a template's components when required. Have separate pages for each Python project. Using axios like you did in the devops sprint to connect to a running API and output the results.

<br><br>


## **autogenerate_gym_calendar**<br>
**Language**: React<br>
**Date Started**: 2022-10-15<br>
**Overview**: Investigate into whether it is possible to add events to your calendar given a form, just like barbers do. If you can, add a form to add your next week's gym schedule. There may be issues with adding to the correct calendar.

<br><br>


<br>

## Completed Project Ideas

---
<br>


## **python_template**<br>
**Date Started**: 2022-09-15<br>
**Date Completed**: 2022-09-15 (1 day)<br>
**Language**: Python<br>
**Overview**: A template for later Python projects. Containing:
- cookiecutter - A template for the whole project.
- tox - So that we can use pydocstyle and pycodestyle.
- .env - For environment variables.
- test folder - To store tests.
- README
- Example .py module  - Make it reference an environment variable and have a example method that can be run (and how to run it).
- .gitignore - Git has default ones.<br>

**Result**: I now have a cookiecutter template up and running for future Python projects.<br>
**Running the Project**: You can call the cookiecutter template by downloading it to your machine and running:
- "cd...".
- "cookiecutter ~/Documents/python_projects/python_template". <br><br>


## **basic_messaging**<br>
**Date Started**: 2022-09-17<br>
**Date Completed**: 2022-09-17 (1 day)<br>
**Language**: Python<br>
**Overview**: A basic messaging app. Effectively a prerequisite for tcp_message_sender_and_receiver. Use Flask to send a string from one endpoint (host:port pair) to another Python script.<br>
**Result**: You can now send and receive a TCP or UDP message between a server (receiver) and client (sender).
**Running the Project**: You can run the code in the terminal by running:
- Terminal 1: "python receiver.py udp".
- Terminal 2: "python sender.py udp".

You may need to update the host and port.<br><br>


## **muscle_checker**<br>
**Date Started**: 2022-09-29<br>
**Date Completed**: 2022-10-09 (10 days)<br>
**Language**: Python<br>
**Overview**: Input which exercises you completed this week. The system outputs which of the main muscles you missed this week and what exercises you could do to train them.<br>
**Result**: I now have a muscle_checker Flask website which can be run anytime and outputs the muscles hit, muscles missed and what exercises to do to hit them.<br>
**Running the Project**: To run the project, follow these steps:
- Run "git clone ...".
- cd into the muscle_checker directory.
- Run "python3 -m venv venv" to create a new virtual environment to run the project inside.
- Run ". venv/bin/activate" to activate the new environment.
- Run "flask run --host=0.0.0.0" to start running the website.
- Go to "127.0.0.1:5000".
<br><br>
