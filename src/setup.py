# Copyright (c) 2019 Monolix
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from setuptools import setup

def get_file_conts(file):
    with open(file, "r") as f:
        contents = f.read()
    
    return contents

requirements = get_file_conts("./requirements.txt").split("\n")

dependencies = [line for line in requirements 
    if not line.startswith("//") or line != ""]

setup(
    name="teddy",
    version="0.1.0",
    description="Doc generator for Python.",
    long_description=get_file_conts("../README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/monolix/teddy",
    author="Monolix",
    author_email="monolix.team@gmail.com",
    license="MIT",
    packages=["teddy"],
    install_requires=dependencies,
    zip_safe=False
)