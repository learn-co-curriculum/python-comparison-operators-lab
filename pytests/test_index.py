import pytest
from ipynb.fs.full.index import *

def test_boolean_compare():
    assert boolean_compare == False
    assert boolean_compare2 == False

def test_number_compare():
    assert number_compare == True
    assert number_compare2 == True
    assert number_compare3 == False

def test_string_compare():
    assert string_compare == True
    assert string_compare2 == False
    assert string_compare3 == True

def test_list_compare():
    assert list_compare == True
    assert list_compare2 == True
    assert list_compare3 == False
    assert list_compare4 == True
    assert list_compare5 == False

def test_logical_compare():
    assert logical_compare == []
    assert logical_compare2 == True
    assert logical_compare3 == 0
    assert logical_compare4 == 2
    assert logical_compare5 == 2
    assert logical_compare6 == False
    assert logical_compare7 == False

def test_identity_compare():
    assert identity_compare == False
    assert identity_compare2 == True
    assert identity_compare3 == True
    assert identity_compare4 == True
    assert identity_compare5 == False
    assert identity_compare6 == False
