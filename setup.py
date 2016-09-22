#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python_histogram_analysis_extractor',
    version='0.0.1',
    description="Extract the histrogram from an image and analyse",
    long_description=readme + '\n\n',
    author="Shane Devane",
    author_email='shanedevane@gmail.com',
    url='https://github.com/shanedevane/python_histogram_analysis_extractor',
    packages=[
        'python_histogram_analysis_extractor',
    ],
    package_dir={'python_histogram_analysis_extractor':
                 'python_histogram_analysis_extractor'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_histogram_analysis_extractor',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
