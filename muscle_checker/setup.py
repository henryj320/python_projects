"""Setup file."""
import setuptools
from setuptools import setup

setup(
    name="muscle_checker",
    version="1.0",
    description="""Input which exercises you completed this week. The system outputs
    which of the main muscles you missed this week and what exercises you could do to train them.""",
    author="Henry James",
    author_email="henryj320@gmail.com",
    packages=setuptools.find_packages(where="src", exclude=("tests",)),
    install_requires=[], # external packages required
    python_requires=">=3.8"
)
