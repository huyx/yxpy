# -*- coding: utf-8 -*-
from distutils.core import setup
import os.path

version = '0.1.4'

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]

def read(fname):
    fname = os.path.join(os.path.dirname(__file__), fname)
    return open(fname).read().strip()

def read_files(*fnames):
    return '\r\n\r\n\r\n'.join(map(read, fnames))

setup(
    name = 'yxpy',
    version = version,
    packages = ['yxpy'],
    description = 'Python utils',
    long_description = read_files('README.rst', 'CHANGES.rst'),
    author = 'huyx',
    author_email = 'ycyuxin@gmail.com',
    url = 'https://github.com/huyx/yxpy',
    keywords = ['python', 'util'],
    classifiers = classifiers, 
    )
