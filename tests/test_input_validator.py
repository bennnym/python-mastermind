from validator.input_validator import InputValidator
from validator.rules.guess_length_rule import GuessLengthRule
from validator.rules.valid_colour_rule import ValidColourRule

import pytest


@pytest.fixture
def initialise_validator():
    rules = [GuessLengthRule(), ValidColourRule()]
    return InputValidator(rules)

def test_guess_length_rule(initialise_validator):    
    user_input = ["Red", "Red", "Red", "Red", "Red"]
    
    valid_input = initialise_validator.validate(user_input)
    
    assert not valid_input
    

def test_valid_colour_rule(initialise_validator):
    user_input = ["Red", "Red", "Red", "Red", "Pink"]

    valid_input = initialise_validator.validate(user_input)

    assert not valid_input
    
