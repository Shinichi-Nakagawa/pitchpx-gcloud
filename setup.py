#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

__author__ = 'Shinichi Nakagawa'


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    return ''


setup(
    name='pitchpx-gcloud',
    version='0.1.0',
    description='MLBAM Gameday dataset converter(for Google Cloud)',
    long_description=read_file('README.rst'),
    author='Shinichi Nakagawa',
    author_email='spirits.is.my.rader@gmail.com',
    url='https://github.com/Shinichi-Nakagawa/pitchpx-gcloud',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['baseball', 'MLB', 'MLBAM', 'SABRmetrics', 'SABR', 'Major league baseball', 'pitchpx'],
    license='MIT License',
    install_requires=[
        'google-api-python-client',
        'click',
        'gspread',
    ],
    entry_points="""
        [console_scripts]
        pitchpx = pitchpx-gcloud:main
    """,
)
