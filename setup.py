# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pacMASS", # Replace with your own username
    version="0.0.1",
    author="Jürgen Claesen",
    author_email="jurgen.claesen@gmail.com",
    description="A package to estimate the elemental composition of peptides and proteins based on the monoisotopic mass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jclaesen/pacMASS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

