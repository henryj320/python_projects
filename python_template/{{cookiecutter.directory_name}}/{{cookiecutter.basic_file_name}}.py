"""A basic Python script to check that everything is working."""
import os
from dotenv import load_dotenv

load_dotenv()  # Allows you to reference env variables with os.environ.get()

print("Hello, {{cookiecutter.greeting_recipient}}!")
print(os.environ.get("USE_ENVS"))
