#!/usr/bin/env python
"""Setup script for iperf3-cython-wrapper"""
from setuptools import find_packages, setup, Extension
import codecs
import os
import re

from Cython.Build import cythonize

EXTENSIONS = [
    Extension(
        'c_iperf3.c_iperf3',
        sources=[os.path.join('c_iperf3', 'c_iperf3.pyx')],
        libraries=['iperf']
    )
]


def get_long_description():
    """Reads the main README.rst to get the program's long description"""
    with codecs.open('README.rst', 'r', 'utf-8') as f_readme:
        return f_readme.read()


def get_package_metadata(attribute):
    """Reads metadata from the main package's __init__"""
    with open(os.path.join('c_iperf3', '__init__.py'), 'r') as f_init:
        return re.search(
            r'^__{attr}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(attr=attribute),
            f_init.read(), re.MULTILINE
        ).group(1)


setup(
    name=get_package_metadata('title'),
    version=get_package_metadata('version'),
    description=get_package_metadata('brief'),
    long_description=get_long_description(),
    author=get_package_metadata('author'),
    maintainer='VirtualTam',
    maintainer_email='virtualtam@flibidi.net',
    license='MIT',
    url='https://github.com/virtualtam/iperf3-cython-wrapper',
    keywords='network throughput iperf3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ],
    ext_modules=cythonize(EXTENSIONS)
)
