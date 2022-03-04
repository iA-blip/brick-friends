from setuptools import setup, find_packages

with open("LICENSE") as f:
    license = f.read()

setup(
    name="brick-friends",
    version="1.0",
    description="Command-line tool to friend people on brick-hill.",
    author="iA-blip",
    license=license,
    packages=find_packages(exclude=("docs")),
    entry_points={
        "console_scripts": [
            "brick-friends=src.cli:main"
        ],
    }
)