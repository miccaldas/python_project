"""Automates the creation of package documentation and
   instals it locally."""
import os
import shutil
import stat
import subprocess
import time

# import snoop
# from snoop import pp


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
        self.config_path = os.path.join(self.sub_path, "configs")
        os.mkdir(self.config_path)
        self.partials_path = os.path.join(self.sub_path, "partials")
        os.mkdir(self.partials_path)

    # @snoop
    def manifest(self):
        """Creates file that itemizes all non-code files needed
        to run the program, and their paths."""
        manif_file = f"{self.path}/MANIFEST.in"
        with open(manif_file, "w") as manifest:
            manifest.write(f"include {self.folder_name}/README.md")

    # @snoop
    def gitignore(self):
        """Creates file that defines what files Git should ignore."""
        cmd = "git-ignore -u python > '.gitignore'"
        subprocess.run(cmd, cwd=self.path, shell=True)

    # @snoop
    def license(self):
        """The copyright license of the project."""
        license_file = f"{self.path}/LICENSE"
        with open(license_file, "w") as license:
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

    # @snoop
    def pyproject(self):
        """Document that states that we're using setuptools and pip wheel."""
        pyproject_file = f"{self.path}/pyproject.toml"
        with open(pyproject_file, "w") as pyproject:
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

    # @snoop
    def readme(self):
        """Long form presentation of the project."""
        readme_file = f"{self.path}/README.md"
        with open(readme_file, "w") as readme:
            readme.write("\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)")

    # @snoop
    def setup(self):
        """Project's metadata."""
        setup_file = f"{self.path}/setup.cfg"
        with open(setup_file, "w") as setup:
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
            setup.write("    click")
            setup.write("\n")
            setup.write("show_source = True")
            setup.write("\n")
            setup.write("\n")
            setup.write("[flake8]")
            setup.write("\n")
            setup.write("extend-ignore = F401 F841 W605 E704, E722, E1, W1, E2, W2, E3, W3, E4, W4, E5, W5, E731")
            setup.write("\n")
            setup.write("max-line-length = 180")
            setup.write("\n")
            setup.write("verbose = 2")
            setup.write("\n")
            setup.write("show-source = True")
            setup.write("\n\n")
            setup.write("[pdbr]\n")
            setup.write("style = yellow\n")
            setup.write("use_traceback = True\n")
            setup.write("theme = friendly\n\n")
            setup.write("[options.entry_points]")
            setup.write("\n")
            setup.write("    console_scripts =\n")

    # @snoop
    def init(self):
        """Empty folder that signifies to python that the
        folder is part of a package."""
        init_sub_file = f"{self.sub_path}/__init__.py"
        init_conf_file = f"{self.config_path}/__init__.py"
        for ini in [init_sub_file, init_conf_file]:
            with open(ini, "w") as init:
                init.write(" ")

    # @snoop
    def config(self):
        """Folder to house all configuration files"""
        cmd = f"cp ~/python/reusable_files/reusable_files/configs/* {self.config_path}"
        subprocess.run(cmd, shell=True)

    # @snoop
    def partials(self):
        """Folder to house all code partials"""
        cmd = f"cp ~/python/reusable_files/reusable_files/partials/* {self.partials_path}"
        subprocess.run(cmd, shell=True)

    # @snoop
    def add_to_path(self):
        """
        Adds new project to PYTHONPATH
        """
        with open(f"{self.sub_path}/python_path.sh", "w") as pth:
            pth.write('sed -ri "$ s/.$/:\\x2Fhome\\x2Fmic\\x2Fpython\\x2F' + self.folder_name + '\\x22/g" "/home/mic/.zshenv"')
        cmd = f"chmod +x '{self.sub_path}/python_path.sh'"
        subprocess.run(cmd, cwd=self.sub_path, shell=True)
        zsh = subprocess.run(f"{self.sub_path}/python_path.sh", shell=True, stdout=subprocess.PIPE)
        print(f"The results are, {zsh.stdout}")
        subprocess.run("source ~/.zshenv", shell=True)
        subprocess.run(f"/usr/bin/trash-put '{self.sub_path}/python_path.sh'", shell=True)

    # @snoop
    def git(self):
        """Initiates a new git repository."""
        self.gitinit("git init -b master")
        self.gitinit("git add .")
        self.gitinit("git commit -m 'First Commit'")
        self.gitinit("gh auth login --with-token < ~/documentation/github_personal_access_token")
        self.gitinit(f"gh repo create {self.folder_name} --disable-issues --disable-wiki --public --remote=origin_github --source=. --push")

    # Suggested by Sourcery
    def gitinit(self, arg0):
        cmd_create = arg0
        subprocess.run(cmd_create, cwd=self.path, shell=True)
        time.sleep(2)


if __name__ == "__main__":
    Builder()
