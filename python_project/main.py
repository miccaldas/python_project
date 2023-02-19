"""Module that'll call the methods defined on 'project_builder.py'."""

import subprocess

import click
import isort  # noqa: F401
import snoop
from loguru import logger

from python_project.Builder import Builder

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@snoop
def main():
    """Here we'll ask the user for input to define the value of
    the instance variable and pass it to the Builder class."""

    name = input(click.style("[?] - What is the name of your project? ", fg="bright_white", bold=True))

    build = Builder(name)
    build.create_folders()
    build.manifest()
    build.gitignore()
    build.license()
    build.pyproject()
    build.readme()
    build.setup()
    build.init()
    build.db_calls_explanation()
    build.dummy_file()
    build.call_file_creator()
    build.add_to_path()
    build.git()


if __name__ == "__main__":
    main()
