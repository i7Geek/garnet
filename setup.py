import pathlib

from setuptools import find_packages, setup

try:
    from pip.req import parse_requirements
except ImportError:  # pip >= 10.0.0
    from pip._internal.req import parse_requirements


WORK_DIR = pathlib.Path(__file__).parent


with open("readme.rst", "r", encoding="utf-8") as f:
    description = f.read()


def get_requirements():
    """
    Read requirements from 'requirements txt'
    :return: requirements
    :rtype: list
    """
    file = WORK_DIR / "requirements.txt"

    install_reqs = parse_requirements(str(file), session="hack")
    return [str(ir.req) for ir in install_reqs]


setup(
    name="pomegranate",
    version="0.1.1",
    packages=find_packages(exclude=("examples.*",)),
    url="https://github.com/uwinx/pomegranate",
    license="MIT",
    author="Martin Winks",
    requires_python=">=3.5",
    author_email="mpa@snejugal.ru",
    description="Pomegranate is small telethon add-on",
    long_description=description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=get_requirements(),
    package_data={"": ["requirements.txt"]},
    include_package_data=False,
    keywords="add-on telethon fsm",
)
