#!/usr/bin/env python

import sys
import os
from setuptools import setup


_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))

del sys.path[0]
README = open(os.path.join(_top_dir, 'README.md')).read()

import simplerestler

setup(
    name='simplerestler',
    version=simplerestler.__version__,
    description="Simple reStructuredText Builder",
    long_description=README,
    
    author='Svilborg',
    author_email='',
    maintainer='Svilborg',
    maintainer_email='',
    url='http://github.com/svilborg/simplerestler',

    classifiers=[c.strip() for c in """
        Development Status :: 1 - Planning
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2        
        Programming Language :: Python :: 2.7
        Topic :: Software Development :: Libraries :: Python Modules
        """.split('\n') if c.strip()],
    keywords='Simple reStructuredText Builder',

    license='MIT',
    py_modules=["simplerestler"],
    package_dir={"simplerestler": "simplerestler"},
    include_package_data=True,
    zip_safe=False,
)

