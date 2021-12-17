"""Automates the creation of package documentation and
   instals it locally."""
import os
import subprocess
import time

import fire
import isort  # noqa: F401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


class Builder:
    """Builds some boilerplate about python packages. The files
    are built on the spot, and should be completed at a later
    time."""

    def __init__(self, folder_name):
        self.folder_name = folder_name

    @logger.catch
    def create_folders(self):
        """Creates the primary folders."""
        parent_dir = os.getcwd()
        self.path = os.path.join(parent_dir, self.folder_name)
        os.mkdir(self.path)
        self.sub_path = os.path.join(self.path, self.folder_name)
        os.mkdir(self.sub_path)

    @logger.catch
    def manifest(self):
        """Creates file that itemizes all non-code files needed
        to run the program, and their paths."""
        manif_file = f"{self.path}/MANIFEST.in"
        manifest = open(manif_file, "w")
        manifest.write(f"include {self.folder_name}/README.md")
        manifest.close()

    @logger.catch
    def gitignore(self):
        """Creates file that defines what files Git should ignore."""
        ignore_file = f"{self.path}/.gitignore"
        ignore = open(ignore_file, "w")
        ignore.write("# Compiled python modules.")
        ignore.write("\n")
        ignore.write("*.pyc")
        ignore.write("\n")
        ignore.write("\n")
        ignore.write("# Setuptools distribution folder.")
        ignore.write("\n")
        ignore.write("/dist/")
        ignore.write("\n")
        ignore.write("\n")
        ignore.write("# Python egg metadata, regenerated from source files by setuptools.")
        ignore.write("\n")
        ignore.write("/*.egg-info")
        ignore.close()

    @logger.catch
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

    @logger.catch
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
        pyproject.close()

    @logger.catch
    def readme(self):
        """Long form presentation of the project."""
        readme_file = f"{self.path}/README.md"
        readme = open(readme_file, "w")
        readme.write(" ")
        readme.close()

    @logger.catch
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
        setup.write(
            """classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent"""
        )
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
        setup.write("\n")
        setup.write("[flake8]")
        setup.write("\n")
        setup.write("extend-ignore = E501")
        setup.write("\n")
        setup.write("verbose = 2")
        setup.write("\n")
        setup.write("show-source = True")
        setup.close()

    @logger.catch
    def init(self):
        """Empty folder that signifies to python that the
        folder is parto fo a package."""
        init_file = f"{self.sub_path}/__init__.py"
        init = open(init_file, "w")
        init.write(" ")
        init.close()

    @logger.catch
    def git(self):
        """Does the first commit of a new git repository."""
        cmd_init = "git init -b master"
        subprocess.run(cmd_init, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_add = "git add ."
        subprocess.run(cmd_add, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_commit = 'git commit -m "First commit"'
        subprocess.run(cmd_commit, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_origin = f"git remote add origin git@notabug.org:micaldas/{self.folder_name}.git"
        subprocess.run(cmd_origin, cwd=self.path, shell=True)
        time.sleep(2)
        cmd_push = "git push -u origin master"
        subprocess.run(cmd_push, cwd=self.path, shell=True)


if __name__ == "__main__":
    fire.Fire(Builder)

"""
build = Builder("teste", "https://notabug.org/micaldas/teste.git")
build.create_folders()
build.manifest()
build.gitignore()
build.license()
build.pyproject()
build.readme()
build.setup()
build.init()
build.git()"""
