"""A basic Python script to check that everything is working."""
import os
# from dotenv import load_dotenv
from dataclasses import dataclass, fields
from typing import Dict, List
import json

# load_dotenv()  # Allows you to reference env variables with os.environ.get()

@dataclass
class Group:
    """Dataclass to hold the Group:Muscles"""
    name: str
    muscles: List

@dataclass
class Muscle:
    """Dataclass to hold Muscle:Exercises"""
    name: str
    exercises: List

# print(os.environ.get("USE_ENVS"))


def json_file_to_dict(file) -> dict:
  
    json_file = open(file)  # Opens the JSON file.
  
    return json.load(json_file)  # Extracts the data from the JSON file.


groups = json_file_to_dict('all_muscles.json')