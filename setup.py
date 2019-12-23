from setuptools import find_packages, setup

NAME = "simgeo"

install_requires=[
    "numpy"
]

dev_requires = install_requires[:]
tests_requires = install_requires[:] + [
    "pytest",
    "pytest-cov",
]

style_requires = [
    "flake8",
    "wemake-python-styleguide",
    "pydocstyle",
    # typechecking
    # "typeshed",
    # "mypy",
]

setup(
    name=NAME,
    install_requires=install_requires,
    packages=find_packages(exclude=("tests",)),
    extras_require={"dev": dev_requires, "test": tests_requires, "style": style_requires},
)
