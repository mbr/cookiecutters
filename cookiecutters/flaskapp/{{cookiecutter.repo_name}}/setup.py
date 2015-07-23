#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='{{cookiecutter.repo_name}}',
    version='0.1.dev1',
    description='',
    long_description=read('README.rst'),
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='http://github.com/mbr/{{cookiecutter.repo_name}}',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.repo_name}} = {{cookiecutter.repo_name}}.cli:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 3',
    ]
)
