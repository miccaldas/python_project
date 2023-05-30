"""Module that'll call the methods defined on 'project_builder.py'."""

import subprocess

import click
from Builder import Builder

# import snoop


subprocess.run(["isort", __file__])


# @snoop
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
    build.config()
    build.partials()
    build.add_to_path()
    build.git()


if __name__ == "__main__":
    main()
