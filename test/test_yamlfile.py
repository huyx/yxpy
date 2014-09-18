# -*- coding: utf-8 -*-
from yxpy import yamlfile

def test_load():
    data = yamlfile.load('test/data/yamlfile/main.yaml')
    assert data['name'] == 'main'
    assert data['a']['name'] == 'a'
    assert data['a']['aa']['name'] == 'aa'
