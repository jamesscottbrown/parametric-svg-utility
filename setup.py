import os

from setuptools import setup

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="parametric-svg-utility",
    description="Apply transformations to Parametric SVG files",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="James Scott-Brown",
    author_email="james@jamesscottbrown.com",
    url="https://github.com/jamesscottbrown/parametric-svg-utility",
    project_urls={
        "Source": "https://github.com/jamesscottbrown/parametric-svg-utility",
        "Issues": "https://github.com/jamesscottbrown/parametric-svg-utility/issues",
    },
    classifiers=[],
    keywords="",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["parametric_svg_utility"],
    entry_points="""
        [console_scripts]
        parametric-svg-utility=parametric_svg_utility.cli:cli
    """,
    install_requires=[
        "cairosvg",
        "click",
        "sympy"
    ],
    extras_require={"test": ["pytest"]},
    tests_require=["parametric-svg-utility[test]"],
)
