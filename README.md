# python_projects
Last update: 2022/10/07 12:37
<br><br>

## Future Project Ideas

---
<br>

**Title**: watt_checker<br>
**Language**: Python / Powershell<br>
**Overview**: Records the Watts-used by the laptop every 30 minutes. Record the value into an Excel spreadsheet so that a chart can be automatically generated or updated every day. Alternatively, use Python so that matplotlib and seaborn can be used. On brief research, it is not easy to grab the current power draw of a computer. Intel has some built-in, but may be complicated.<br><br>

**Title**: weekly_goals_GUI<br>
**Language**: Python<br>
**Overview**: Shows a progress bar for your weekly goals. For example, a progress bar on how close to your reading goal you are. You could also autorun this on startup and set your background to the progress bars by screenshotting and setting as the wallpaper. It could also show how much of your 7.5 * 5 hrs of work you've done so far. You could run this via Flask. This would make it so that you can use Python (storing values in .txt files) and a clean webpage with Bootstrap. Alternatively, you could use React for clean elements and running.<br><br>

**Title**: wifi_users_tracker<br>
**Language**: Linux Script<br>
**Overview**: A software which states when a new device joins your WiFi network via a notification. It could be extended to show when a device disconnects. Previous implementation of this used a for loop to read the nmap's "x devices found" string.<br><br>

**Title**: transcripter<br>
**Language**: Python<br>
**Overview**: Learn how to make a transcripter that converts speech to text. Look into any existing libraries that allow for this.<br><br>

**Title**: internet_stability_recorder<br>
**Language**: Python<br>
**Overview**: Sends a ping every 5 minutes and records the result to Excel. Use the results to automatically plot into a chart. This would show how stable the internet is throughout the day.<br><br>

**Title**: centre_country_shower<br>
**Language**: Python<br>
**Overview**: Shows the centre of a given country based on different factors: geological, average age, population, etc. This would show age densities, etc.<br><br>

**Title**: running_route_generator<br>
**Language**: Python<br>
**Overview**: The user provides a location. The script generates a path to coordinates x metres away and adds this as a route on Google Maps and outputs this to the user. This allows the user to run to a random place every time the exact distance away that they want.<br><br>

**Title**: tcp_message_sender_and_receiver<br>
**Language**: Python<br>
**Overview**: Write a program that sends and receives message from the basics. Generate a TCP segment with all of the fields in binary. Set up a port to send on and a port to receive on. Use your Java code as a reference. Importantly, the receiver needs to be listening on the port. Use datasubs to find how to run an app on a certain portand listen to requests. Set out the plan logically.<br><br>

**Title**: height_determination_software<br>
**Language**: Not a clue<br>
**Overview**: Use vanishing points to determine the height of individuals or objects inside photos. (Fspy)<br><br>

**Title**: blender_addon_forensic_tool<br>
**Language**: Python <br>
**Overview**: Creating simulations, blah, blah, blah.<br><br>

**Title**: computer_writing_tool<br>
**Language**: Not a clue<br>
**Overview**: Piece of software that analyses text, categorises words into groups (verbs, nouns, prepositions, etc.) and uses preset knowledge on sentence structures to write sentences/more.<br><br>

**Title**: dnd_map_precedural_gen_tool<br>
**Language**: Not a clue <br>
**Overview**: Precedurally generates tools in different settings for use by DMs and GMs in TTRPG campaigns. Different settings can be changed to tweak results. <br><br>

**Title**: text_to_music<br>
**Language**: not a clue <br>
**Overview**: Converts text to music based on a formula. Including tone reading through negativity/positivity of words in sentence, (minor/major). https://www.youtube.com/watch?v=PVT6WpOyf0s&feature=youtu.be<br><br>

**Title**: precedurally_generated_evolution_of_civilisation <br>
**Language**: Not a clue<br>
**Overview**: Tweak parameters as the civilisation and planet evolves to create stats and planet image.<br><br>

**Title**: dnd_fun_tool<br>
**Language**: Not a clue <br>
**Overview**: Keep track of characters, better combat system, better image display system, better tools for DM.<br><br>

**Title**: Free_Worlds_website<br>
**Language**: HTML/Javascript<br>
**Overview**: website go brr.<br><br>

**Title**: full_system_search<br>
**Language**: Python<br>
**Overview**: Similar to DocumentSystem to Git. Make a program that takes a searchterm and searches the entire computer for any documents named or containing the term. Make it show sections at a time with a progress bar to learn Python progress bars in the terminal. Add a parameter for OS so that OS files can be ignored. Output should be something like "Found: X occurrences of "example" in Documents, Y occurences of "example" in Pictures.<br><br>

**Title**: muscle_checker<br>
**Language**: Python<br>
**Overview**: Input which exercises you completed this week. The system outputs which of the main muscles you missed this week and what exercises you could do to train them.<br><br>


<br>
<h2>Completed Project Ideas</h2>
<hr>

**Title**: python_template<br>
<strong>Date Completed:</strong> 2022-09-15<br>
**Language**: Python<br>
**Overview**: A template for later Python projects. Containing:
<br><strike><i>cookiecutter</i> - A template for the whole project.</strike>
<br><strike><i>tox</i>  - So that we can use pydocstyle and pycodestyle.</strike>
<br><strike><i>.env</i>  - For environment variables.</strike>
<br><strike><i>test folder</i>  - To store tests.</strike>
<br><strike><i>README</i></strike>
<br><strike><i>Example .py module</i>  - Make it reference an environment variable and have a example method that can be run (and how to run it)</strike>
<br><strike><i>.gitignore</i>  - Git has default ones</strike><br>
<strong>Result:</strong> I now have a cookiecutter template up and running for future Python projects. You can call the cookiecutter template by downloading it to your machine and running:<br>
<i>cd... </i><br>
<i>cookiecutter ~/Documents/python_projects/python_template</i>
<br><br>

**Title**: basic_messaging<br>
<strong>Date Completed:</strong> 2022-09-17<br>
**Language**: Python<br>
**Overview**: A basic messaging app. Effectively a prerequisite for tcp_message_sender_and_receiver. Use Flask to send a string from one endpoint (host:port pair) to another Python script.<br>
<strong>Result:</strong> You can now send and receive a TCP or UDP message between a server (receiver) and client (sender). You can run the code in the terminal by running:<br>
Terminal 1: <i>python receiver.py udp</i><br>
Terminal 2: <i>python sender.py udp</i><br>
You may need to update the host and port.
<br><br>
