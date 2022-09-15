"""Setup file."""
import setuptools
from setuptools import setup

setup(
    name="project_name",
    version="1.0",
    description="project_description",
    author="Henry James",
    author_email="henryj320@gmail.com",
    packages=setuptools.find_packages(where="src", exclude=("tests",)),
    install_requires=[], # external packages required
    python_requires=">=3.8"
)
