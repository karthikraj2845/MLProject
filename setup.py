from setuptools import setup, find_packages
from typing import List
HYPENATE = '-e .'
def get_requirements(file_path: str) -> list:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPENATE in requirements:            requirements.remove(HYPENATE)
    return requirements
setup(
    name="ML-Project",
    version="0.0.1",
    author="Karthik",
    author_email="karthikrajpuduri@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)