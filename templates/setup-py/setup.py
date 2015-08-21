#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

{%- if readme_file %}

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

{%- endif %}

setup(
    name='{{project_name}}',
    version='{{version}}',
    description='{{description}}',
    {%- if readme_file %}
    long_description=read('{{readme_file}}'),
    {%- endif %}
    author='{{user_full_name}}',
    author_email='{{user_email}}',
    {%- if github_project == "yes" %}
    url='https://github.com/{{user_github_account}}/{{project_name}}',
    {%- endif %}
    license='{{license}}',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    {%- if entry_point %}
    entry_points={
        'console_scripts': [
            '{{entry_point}} = {{project_name}}:cli.cli',
        ],
    },
    {%- endif %}
    classifiers=[
        'Programming Language :: Python :: {{python_version}}',
    ]
)
