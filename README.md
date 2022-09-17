# python_projects
Last update: 2022-09-16 00:07
<br /><br />
<h2>Future Project Ideas</h2>
<hr>

<strong>Title:</strong> watt_checker<br />
<strong>Language:</strong> Python / Powershell<br />
<strong>Overview:</strong> Records the Watts-used by the laptop every 30 minutes. Record the value into an Excel spreadsheet so that a chart can be automatically generated or updated every day. Alternatively, use Python so that matplotlib and seaborn can be used. On brief research, it is not easy to grab the current power draw of a computer. Intel has some built-in, but may be complicated.<br /><br />

<strong>Title:</strong> weekly_goals_GUI<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> Shows a progress bar for your weekly goals. For example, a progress bar on how close to your reading goal you are. You could also autorun this on startup and set your background to the progress bars by screenshotting and setting as the wallpaper. It could also show how much of your 7.5 * 5 hrs of work you've done so far.<br /><br />

<strong>Title:</strong> total_screentime<br />
<strong>Language:</strong> Android<br />
<strong>Overview:</strong> Records the screentime you have across all your devices, not just your mobile phone. May require some database or message sending between devices.<br /><br />

<strong>Title:</strong> wifi_users_tracker<br />
<strong>Language:</strong> Linux Script<br />
<strong>Overview:</strong> A software which states when a new device joins your WiFi network via a notification. It could be extended to show when a device disconnects. Previous implementation of this used a for loop to read the nmap's "x devices found" string.<br /><br />

<strong>Title:</strong> transcripter<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> Learn how to make a transcripter that converts speech to text. Look into any existing libraries that allow for this.<br /><br />

<strong>Title:</strong> internet_stability_recorder<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> Sends a ping every 5 minutes and records the result to Excel. Use the results to automatically plot into a chart. This would show how stable the internet is throughout the day.<br /><br />

<strong>Title:</strong> centre_country_shower<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> Shows the centre of a given country based on different factors: geological, average age, population, etc. This would show age densities, etc.<br /><br />

<strong>Title:</strong> treasure_find<br />
<strong>Language:</strong> Android<br />
<strong>Overview:</strong> A fun running game. Places x items in a random location within y metres. The user "picks them up" when within 10 metres. Run ends when the last has been picked up. Show the locations at the end.<br /><br />

<strong>Title:</strong> running_route_generator<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> The user provides a location. The script generates a path to coordinates x metres away and adds this as a route on Google Maps and outputs this to the user. This allows the user to run to a random place every time the exact distance away that they want.<br /><br />

<strong>Title:</strong> tcp_message_sender_and_receiver<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> Write a program that sends and receives message from the basics. Generate a TCP segment with all of the fields in binary. Set up a port to send on and a port to receive on. Use your Java code as a reference. Importantly, the receiver needs to be listening on the port. Use datasubs to find how to run an app on a certain portand listen to requests. Set out the plan logically.<br /><br />

<strong>Title:</strong> height_determination_software<br />
<strong>Language:</strong> Not a clue<br />
<strong>Overview:</strong> Use vanishing points to determine the height of individuals or objects inside photos. (Fspy)<br /><br />

<strong>Title:</strong> blender_addon_forensic_tool<br />
<strong>Language:</strong> Python <br />
<strong>Overview:</strong> Creating simulations, blah, blah, blah.<br /><br />

<strong>Title:</strong> computer_writing_tool<br />
<strong>Language:</strong> Not a clue<br />
<strong>Overview:</strong> Piece of software that analyses text, categorises words into groups (verbs, nouns, prepositions, etc.) and uses preset knowledge on sentence structures to write sentences/more.<br /><br />

<strong>Title:</strong> dnd_map_precedural_gen_tool<br />
<strong>Language:</strong> Not a clue <br />
<strong>Overview:</strong> Precedurally generates tools in different settings for use by DMs and GMs in TTRPG campaigns. Different settings can be changed to tweak results. <br /><br />

<strong>Title:</strong> text_to_music <br />
<strong>Language:</strong> not a clue <br />
<strong>Overview:</strong> Converts text to music based on a formula. Including tone reading through negativity/positivity of words in sentence, (minor/major). https://www.youtube.com/watch?v=PVT6WpOyf0s&feature=youtu.be<br /><br />

<strong>Title:</strong> precedurally_generated_evolution_of_civilisation <br />
<strong>Language:</strong> Not a clue<br />
<strong>Overview:</strong> Tweak parameters as the civilisation and planet evolves to create stats and planet image.<br /><br />

<strong>Title:</strong> dnd_fun_tool <br />
<strong>Language:</strong> Not a clue <br />
<strong>Overview:</strong> Keep track of characters, better combat system, better image display system, better tools for DM.<br /><br />

<strong>Title:</strong> Free_Worlds_website <br />
<strong>Language:</strong> HTML/Javascript<br />
<strong>Overview:</strong> website go brr.<br /><br />

<strong>Title:</strong> basic_messaging <br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> A basic messaging app. Effectively a prerequisite for tcp_message_sender_and_receiver. Use Flask to send a string from one endpoint (host:port pair) to another Python script.<br /><br />


<br />
<h2>Completed Project Ideas</h2>
<hr>

<strong>Title:</strong> python_template<br />
<strong>Language:</strong> Python<br />
<strong>Overview:</strong> A template for later Python projects. Containing:
<br><strike><i>cookiecutter</i> - A template for the whole project.</strike>
<br><strike><i>tox</i>  - So that we can use pydocstyle and pycodestyle.</strike>
<br><strike><i>.env</i>  - For environment variables.</strike>
<br><strike><i>test folder</i>  - To store tests.</strike>
<br><strike><i>README</i></strike>
<br><strike><i>Example .py module</i>  - Make it reference an environment variable and have a example method that can be run (and how to run it)</strike>
<br><strike><i>.gitignore</i>  - Git has default ones</strike><br />
<strong>Result:</strong> I now have a cookiecutter template up and running for future Python projects. You can call the cookiecutter template by downloading it to your machine and running:<br>
<i>cd... </i><br />
<i>cookiecutter ~/Documents/python_projects/python_template</i>
<br /><br />
