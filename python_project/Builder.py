"""Automates the creation of package documentation and
   instals it locally."""
import os
import shutil
import stat
import subprocess
import sys
import time

import snoop
from snoop import pp


class Builder:
    """Builds some boilerplate about python packages. The files
    are built on the spot, and should be completed at a later
    time."""

    def __init__(self, folder_name):
        self.folder_name = folder_name

    # @snoop
    def create_folders(self):
        """Creates the primary folders."""
        parent_dir = os.getcwd()
        self.path = os.path.join(parent_dir, self.folder_name)
        os.mkdir(self.path)
        self.sub_path = os.path.join(self.path, self.folder_name)
        os.mkdir(self.sub_path)

    # @snoop
    def manifest(self):
        """Creates file that itemizes all non-code files needed
        to run the program, and their paths."""
        manif_file = f"{self.path}/MANIFEST.in"
        manifest = open(manif_file, "w")
        manifest.write(f"include {self.folder_name}/README.md")
        manifest.close()

    # @snoop
    def gitignore(self):
        """Creates file that defines what files Git should ignore."""
        cmd = "git-ignore -u python > '.gitignore'"
        subprocess.run(cmd, cwd=self.path, shell=True)

    # @snoop
    def license(self):
        """The copyright license of the project."""
        license_file = f"{self.path}/LICENSE"
        license = open(license_file, "w")
        license.write(
            """MIT License

            Copyright (c) 2021 James Calam Briggs

            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is
            furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE."""
        )
        license.close()

    # @snoop
    def pyproject(self):
        """Document that states that we're using setuptools and pip wheel."""
        pyproject_file = f"{self.path}/pyproject.toml"
        pyproject = open(pyproject_file, "w")
        pyproject.write("[build-system]")
        pyproject.write("\n")
        pyproject.write("requires = [")
        pyproject.write("\n")
        pyproject.write('    "setuptools>=56",')
        pyproject.write("\n")
        pyproject.write('    "wheel"')
        pyproject.write("\n")
        pyproject.write("]")
        pyproject.write("\n")
        pyproject.write('build-backend = "setuptools.build_meta"')
        pyproject.write("\n\n")
        pyproject.write("[tool.isort]")
        pyproject.write("\n")
        pyproject.write('profile = "black"')
        pyproject.close()

    # @snoop
    def readme(self):
        """Long form presentation of the project."""
        readme_file = f"{self.path}/README.md"
        readme = open(readme_file, "w")
        readme.write(
            "\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)"
        )
        readme.close()

    # @snoop
    def setup(self):
        """Project's metadata."""
        setup_file = f"{self.path}/setup.cfg"
        setup = open(setup_file, "w")
        setup.write("[metadata]")
        setup.write("\n")
        setup.write("name =")
        setup.write("\n")
        setup.write("version = 0.1")
        setup.write("\n")
        setup.write("author = mclds")
        setup.write("\n")
        setup.write("author_email = mclds@protonmail.com")
        setup.write("\n")
        setup.write("description =")
        setup.write("\n")
        setup.write("long_description = file: README.md")
        setup.write("\n")
        setup.write("url =")
        setup.write("\n")
        setup.write("classifiers =")
        setup.write("\n")
        setup.write("    Programming Language :: Python :: 3.10")
        setup.write("\n")
        setup.write("    Development Status :: 4 - Beta")
        setup.write("\n")
        setup.write("    Environment :: Console")
        setup.write("\n")
        setup.write("    Framework :: Celery")
        setup.write("\n")
        setup.write("    License :: OSI Approved :: MIT License")
        setup.write("\n")
        setup.write("    Operating System :: POSIX :: Linux")
        setup.write("\n")
        setup.write("\n")
        setup.write("[options]")
        setup.write("\n")
        setup.write("packages = find:")
        setup.write("\n")
        setup.write("python_requires = >=3.7")
        setup.write("\n")
        setup.write("include_package_data = True")
        setup.write("\n")
        setup.write("verbose = 2")
        setup.write("\n")
        setup.write("install_requires=")
        setup.write("\n")
        setup.write("    mysql.connector")
        setup.write("\n")
        setup.write("    snoop")
        setup.write("\n")
        setup.write("    isort")
        setup.write("\n")
        setup.write("    click")
        setup.write("\n")
        setup.write("show_source = True")
        setup.write("\n")
        setup.write("\n")
        setup.write("[flake8]")
        setup.write("\n")
        setup.write(
            "extend-ignore = F401 F841 W605 E704, E722, E1, W1, E2, W2, E3, W3, E4, W4, E5, W5, E731"
        )
        setup.write("\n")
        setup.write("max-line-length = 180")
        setup.write("\n")
        setup.write("verbose = 2")
        setup.write("\n")
        setup.write("show-source = True")
        setup.write("\n\n")
        setup.write("[options.entry_points]")
        setup.write("\n")
        setup.write("    console_scripts =\n")

    # @snoop
    def init(self):
        """Empty folder that signifies to python that the
        folder is part of a package."""
        init_file = f"{self.sub_path}/__init__.py"
        init = open(init_file, "w")
        init.write(" ")
        init.close()

    @snoop
    def db_calls_explanation(self):
        """
        I'm trying a new system of managing database calls and
        I'm worried that I'll forget about it or of how it works.
        Because of this, I wrote a short explanation, to get me
        up to speed.
        """
        explanation_file = f"{self.sub_path}/db_calls_explanation.txt"
        exp = open(explanation_file, "w")
        exp.write(
            " We're trying a system of using just one external file to make all database calls.\n"
        )
        exp.write(
            " In any module, if you need to make a db call, instead of writing the code in it,\n"
        )
        exp.write(
            ' you now can uncomment the "from db_call import create_iteration" line in the\n'
        )
        exp.write(
            " begnning of the file, and call it with four arguments. The create_iteration\n"
        )
        exp.write(
            ' function makes a new file, called "call_template.py", with the code needed\n'
        )
        exp.write(
            " for making the connection to MySQL. Afer creating the file, it'll run it and\n"
        )
        exp.write(
            " get whatever informqation was returned. To access the information, just create a\n"
        )
        exp.write(
            " string variable from the 'create_iteration' output. It should always return something.\n"
        )
        exp.write(" The function arguments are these:\n")
        exp.write(" db - Where you choose what database you want to use.\n")
        exp.write(" query - Where you'll write the SQL query to use.\n")
        exp.write(" callend - How to end the MySQL call. You have two options:\n")
        exp.write(" > conn.commit' - when you son't need information back,\n")
        exp.write(" > records = cur.fetchall()' - for when you do.\n")
        exp.write(" ret - Specify what will the function return:\n")
        exp.write(
            " > return records - if you used 'records = cur.fetchall()' before,\n"
        )
        exp.write(" > 'Db call has ran' - if you used 'conn.commit'.\n")
        exp.write(
            " As an example, if you wanted to get all lines from the 'bkmks' database, you would write the following:\n"
        )
        exp.write(
            " create_interaction('bkmks', 'SELECT * FROM bkmks', 'records = cur.fetchall()', 'return records'"
        )
        exp.close()

    @snoop
    def call_file_creator(self):
        """
        This module defines what goes in to the db call.
        It creates a file that'll be used, and reused to
        make them.
        """
        creator = f"{self.sub_path}/"
        shutil.copy(
            "/home/mic/python/reusable_files/_call_file_creator.py", f"{creator}/_call_file_creator.py"
        )

    # @snoop
    def dummy_file(self):
        """
        Because the file 'db_call.py' call on the same file that it
        creates, it needs to import it butin the beginning the file
        doesn't still exists. We'll create a dummy file with the
        same name of the one to import. In that way there will be
        no import errors.
        """
        dum = f'{self.sub_path}/'
        shutil.copy('/home/mic/python/reusable_files/_call_template.py', f'{dum}/_call_template.py')

    @snoop
    def add_to_path(self):
        """
        Adds new project to PYTHONPATH
        """
        pth = open(f"{self.sub_path}/python_path.sh", "w")
        pth.write(
            'sed -ri "$ s/.$/:\\x2Fhome\\x2Fmic\\x2Fpython\\x2F'
            + self.folder_name
            + '\\x22/g" "/home/mic/.zshenv"'
        )
        pth.close()
        cmd = f"chmod +x '{self.sub_path}/python_path.sh'"
        subprocess.run(cmd, cwd=self.sub_path, shell=True)
        zsh = subprocess.run(
            f"{self.sub_path}/python_path.sh", shell=True, stdout=subprocess.PIPE
        )
        print(f"The results are, {zsh.stdout}")
        subprocess.run("source ~/.zshenv", shell=True)

    # @snoop
    def git(self):
        """Initiates a new git repository."""
        cmd_create = "git init -b master"
        subprocess.run(cmd_create, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_add = "git add ."
        subprocess.run(cmd_add, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_commit = "git commit -m 'First Commit'"
        subprocess.run(cmd_commit, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_init = (
            "gh auth login --with-token < ~/documentation/github_personal_access_token"
        )
        subprocess.run(cmd_init, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_repo = f"gh repo create {self.folder_name} --disable-issues --disable-wiki --public --remote=origin_github --source=. --push"
        subprocess.run(cmd_repo, cwd=self.path, shell=True)


if __name__ == "__main__":
    Builder()
