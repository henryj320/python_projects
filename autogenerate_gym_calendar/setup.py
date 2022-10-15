"""Setup file."""
import setuptools
from setuptools import setup

setup(
    name="autogenerate_gym_calendar",
    version="1.0",
    description="Investigate into whether it is possible to add events to your calendar given a form, just like barbers do. If you can, add a form to add your next week's gym schedule. There may be issues with adding to the correct calendar.",
    author="Henry James",
    author_email="henryj320@gmail.com",
    packages=setuptools.find_packages(where="src", exclude=("tests",)),
    install_requires=[], # external packages required
    python_requires=">=3.8"
)
