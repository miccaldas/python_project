from setuptools import setup

setup(
    name="python_project",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Automate the boilerplate of making a python package.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/python_project_mclds",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["python_project"],
    install_requires=[
        "mysql.connector",
        "isort",
        "fire",
        "loguru",
        "click",
    ],
    include_package_data=True,
)
