import pytest
import main

def setup_module(module):
    #init_something()
    pass

def teardown_module(module):
    #teardown_something()
    pass

def test_upper():
    assert 'foo'.upper() == 'FOO'
    
def test_isupper():
    assert 'FOO'.isupper()

def test_1():
    assert main.state_1() == 5
    
#def test_failed_upper():
#    assert 'foo'.upper() == 'FOo'