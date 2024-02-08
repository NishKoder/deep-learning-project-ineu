from typing import List

from setuptools import find_packages, setup


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        requirements = file.read().splitlines()
        requirements = [
            requirement for requirement in requirements
            if not requirement.startswith("-")
        ]
        return requirements


setup(
    name="Xray",
    version="0.0.1",
    author="Nishant Gupta",
    author_email="nishant.apple.app@gmail.com",
    install_requires=get_requirements(file_path="requirements_dev.txt"),
    packages=find_packages()
)
