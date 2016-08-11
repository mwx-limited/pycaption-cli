#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')

dependencies = [
    'pycaption-mwx'
]

setup(
    name='pycaption-cli-mwx',
    version='0.1',
    description='Command line caption conversion',
    author='MWX Limited',
    author_email='mwxltd@gmail.com',
    url='https://github.com/mwx-limited/pycaption-cli-mwx',
    install_requires=dependencies,
    dependency_links = [
        'git+https://github.com/mwx-limited/pycaption-mwx#egg=pycaption-mwx-1.0.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points=dict(
        console_scripts=['pycaption=pycapcli.caption_converter:main']),
)
