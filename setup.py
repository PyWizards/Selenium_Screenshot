import os

from setuptools import find_packages, setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()


# This call to setup() does all the work
setup(
    name="Selenium-Screenshot",
    version="1.7.0",
    description="This package is used to Clipped Images of Html Elements of Selenium Webdriver",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PyWizards/Selenium_Screenshot",
    author="PyWizard org",
    author_email="py.wizard.org@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["Pillow", "selenium"],
    packages=find_packages(exclude=("tests",)),

)