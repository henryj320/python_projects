"""A python script to state which muscles have been missed given calendar text."""
import argparse
from dataclasses import dataclass, fields
from typing import Dict, List
import json
# from dotenv import load_dotenv


@dataclass
class Group:
    """Dataclass to hold the Group:Muscles."""

    name: str
    muscles: List


@dataclass
class Muscle:
    """Dataclass to hold Muscle:Exercises."""

    name: str
    exercises: List


def json_file_to_dict(file: str) -> dict:
    """Take the location of the JSON file and return the JSON.

    Args:
        file (str): The location of the JSON file.

    Returns:
        dict: The JSON data represented as a Python dict.
    """
    json_file = open(file)  # Opens the JSON file.
    return json.load(json_file)  # Extracts the data from the JSON file.


def read_exercises_from_text_file(file: str) -> list:
    """Read the exercises inside of file and convert it into a Python list.

    Args:
        file (str): The location of the JSON file.

    Returns:
        list: A list of the exercises inside of the file inputted.
    """
    with open(file) as opened_file:  # Opens the file and saves each line to lines array.
        lines = opened_file.readlines()

    exercises = []
    for line in lines:  # For loop to grab the exercises.
        # print(line)
        try:  # Only enters if the line contains ":".
            location = line.index(":")
            exercise = str(line)[0:location]  # Grabs the exercise.

            if exercise[0:3] == "Abs":  # Special case to catch the format of "Abs for 8:15".
                exercises.append("Abs")
            else:
                exercises.append(exercise)
        except ValueError:  # Enters if the line does not contain ":".
            pass

    return exercises


def convert_exercises_list_to_dict(session_number: int, all_groups: list, all_muscles: list, hit_exercises: list) -> dict:
    """Take a list of exercises and convert it into JSON, calculating the group and reformatting it.

    Args:
        all_groups (list): A list containing all groups.
        all_muscles (list): A list containing all muscles and associated exercises.
        hit_exercises (list): A list containing the exercises hit.

    Returns:
        json: A JSON object of the exercises.
    """
    hit_muscle_exercises = []  # [ ["Pecs", ["Bench Press", ...]], ["Triceps", ["Tricep Pull-Downs", ...]] ]
    muscle_count = 0
    for muscle in all_muscles:  # For each muscle.

        for exercise in muscle["exercises"]:  # For each exercise.

            for hit_exercise in hit_exercises:  # For each of the exercises hit.

                if hit_exercise == exercise:
                    hit_muscle = all_muscles[muscle_count]["name"]
                    # print(hit_exercise + " which hits " + hit_muscle)

                    muscle_location = -1
                    muscle_exercise_pair_count = 0
                    for muscle_exercise_pair in hit_muscle_exercises:  # For each of the existing muscle:[exercises] pairs.

                        if hit_muscle == muscle_exercise_pair[0]:  # If the hit_muscle is already inside of hit_muscle_exercises.
                            muscle_location = muscle_exercise_pair_count
                            break

                        muscle_exercise_pair_count = muscle_exercise_pair_count + 1

                    if muscle_location == -1:  # If the muscle is not already in hit_muscle_exercises.
                        hit_muscle_exercises.append([hit_muscle, [hit_exercise]])
                    else:  # If the muscle is already in hit_muscle_exercises.
                        hit_muscle_exercises[muscle_location][1].append(hit_exercise)

        muscle_count = muscle_count + 1

    session_group = "Uknown"
    for group in all_groups:  # For each group in all_groups (Push, Pull, Legs, Misc).

        # for hit_muscles in hit_muscle_exercises:
        for muscle in group["muscles"]:
            if hit_muscle_exercises[0][0] == muscle:
                session_group = group["name"]  # Sets the session_group to the correct group name and breaks out of the loops.
                # TODO: This will find the wrong group if you start a session with Abs.

                break

        break

    muscles_json_format = []
    for muscle in hit_muscle_exercises:
        muscles_json_format.append(
            {
                "name": muscle[0],
                "exercises": muscle[1]
            }
        )

    # Creating a dictionary
    session_details_dict = {
        "session_number": session_number,
        "group": session_group,
        "muscles": muscles_json_format
    }

    return session_details_dict


def find_missed_muscles(group: str, hit_muscles: list, all_groups: list) -> list:
    """Given the muscles hit, return a list of muscles missed for the group.

    Args:
        group (str): The muscle group that the hit_muscles are in.
        hit_muscles (list): A list of the muscles hit in the session.
        all_groups (list): Contains all groups, muscles and exercises.

    Returns:
        list: A list containing all of the muscles missed for a given group.
    """
    missed_muscles = []

    correct_group = -1
    count = 0
    for curr_group in all_groups:  # Finds which group in all_groups was hit in the gym session.
        if curr_group["name"] == group:
            correct_group = count
        count = count + 1

    for muscle in all_groups[correct_group]["muscles"]:  # Adds all muscles for that group to missed_muscles.
        missed_muscles.append(muscle)

    for muscle in hit_muscles:  # For each of the muscles hit in the gym session.
        if muscle["name"] in missed_muscles:
            missed_muscles.remove(muscle["name"])  # Remove that muscle from missed_muscles.

    return missed_muscles


def suggested_exercises(all_muscles: str, missed_muscle: str) -> str:
    """Return a string containing all of the exercises you could do to hit the missed muscle.

    Args:
        all_muscles (list): A list containing all muscles and associated exercises.
        missed_muscle (str): The muscle missed.

    Returns:
        str: A string stating which muscle was missed and what exercises to do.
    """
    if missed_muscle == "":
        return ""

    suggested_exercises = f"You didn't train your {missed_muscle}.\nTo train this, you could perform: "
    for curr_muscle in all_muscles:

        if curr_muscle["name"] == missed_muscle:

            for muscle in curr_muscle["exercises"]:

                if muscle == curr_muscle["exercises"][len(curr_muscle["exercises"]) - 1]:

                    suggested_exercises = suggested_exercises[0:len(suggested_exercises) - 2]
                    suggested_exercises += f" or {muscle}.\n"

                else:

                    suggested_exercises += f"{muscle}, "

    return suggested_exercises

    print(all_muscles[0]["exercises"])

    # Add a check if the same exercise comes twice


if __name__ == "__main__":  # Default method to run.

    parser = argparse.ArgumentParser(description="A python script to state which muscles have been missed given calendar text.")  # Allows parsing arguments to the file.
    # parser.add_argument("-f", "--set_calendar_file", help="Sets the location of insert_calendar_text.txt.", default="insert_calendar_text.txt", type=str)
    parser.add_argument("-f", "--file", help="Sets the location of insert_calendar_text.txt.", default="insert_calendar_text.txt", type=str)
    args = parser.parse_args()

    all_muscles = json_file_to_dict('all_muscles.json')
    all_groups = all_muscles["groups"]  # Contains name:[muscles] pairs.
    all_muscles = all_muscles["muscles"]  # Contains name:[exercises] pairs.

    hit_exercises = read_exercises_from_text_file(args.file)
    hit_muscle_exercises = convert_exercises_list_to_dict(1, all_groups, all_muscles, hit_exercises)
    missed_muscles = find_missed_muscles(hit_muscle_exercises["group"], hit_muscle_exercises["muscles"], all_groups)

    print("")
    for muscles in missed_muscles:
        print(suggested_exercises(all_muscles, muscles))
