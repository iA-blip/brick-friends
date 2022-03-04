from setuptools import setup, find_packages

with open("LICENSE") as f:
    license = f.read()

setup(
    name = "brick-friends",
    version = "1.0",
    description = "Command-line tool to friend people on brick-hill.",
    author = "iA-blip",
    url = "https://github.com/iA-blip/brick-friends",
    download_url = "https://github.com/iA-blip/brick-friends/archive/refs/tags/v_01.tar.gz",
    license = license,
    packages = find_packages(),
    keywords = ["brick-hill", "cli"],
    entry_points = {
        "console_scripts": [
            "brick-friends=src.cli:main"
        ],
    },
    install_requires = [
        "argparse",
        "requests",
        "pypac",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Installation/Setup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)