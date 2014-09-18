# -*- coding: utf-8 -*-
"""Load YAML file

Feature:

- support !include tag to include another YAML file
"""
from __future__ import print_function
from yaml.constructor import Constructor
import os.path
import yaml


INCLUDE_TAG = '!include'


def load(filename):
    dirname = os.path.dirname(filename)

    def include(loader, node):
        filename = os.path.join(dirname, loader.construct_scalar(node))
        with open(filename) as f:
            return yaml.load(f)

    Constructor.add_constructor(INCLUDE_TAG, include)

    with open(filename) as f:
        data = yaml.load(f)

    del Constructor.yaml_constructors[INCLUDE_TAG]

    return data
