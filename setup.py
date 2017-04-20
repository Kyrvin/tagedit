#! /bin/python3

from setuptools import setup

setup(
    name='TagEdit',
    version='0.1',
    author='Patrick Keating',
    author_email='kyrvin3@gmail.com',
    url = 'https://github.com/Kyrvin/tagedit',
    description = 'A command line tag editor.',
    packages = ['tagedit'],
    license = 'GNU GPL v2',
    entry_points = {'console_scripts': ['tagedit = tagedit:main']},
    install_requires = ['mutagen']
)
