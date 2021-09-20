import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="RedGram",
    version="0.9.0",
    description="A Simple yet Powerfull TelegramBotApi Lib!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Alirezadigi",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["redgram"],
    include_package_data=True,
    install_requires=["requests"]
)

