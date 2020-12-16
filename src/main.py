from validator.input_validator import InputValidator
from validator.rules.guess_length_rule import GuessLengthRule
from validator.rules.valid_colour_rule import ValidColour


def main():
    guess_length_rule = GuessLengthRule()
    valid_colour_rule = ValidColour()
    
    rules = [guess_length_rule, valid_colour_rule]
    input_validator = InputValidator(rules)

    input_validator.validate(['Orange', 'Orange', 'Orange', 'Pink'])
    
main()

