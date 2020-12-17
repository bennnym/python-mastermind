from mastermind import Mastermind
from hint_checker import HintChecker
from validator.input_validator import InputValidator
from validator.rules.guess_length_rule import GuessLengthRule
from validator.rules.valid_colour_rule import ValidColourRule


def main():
    guess_length_rule = GuessLengthRule()
    valid_colour_rule = ValidColourRule()
    
    rules = [guess_length_rule, valid_colour_rule]
    input_validator = InputValidator(rules)
    hint_checker = HintChecker()

    mastermind = Mastermind(input_validator, hint_checker)
    mastermind.play()
    
main()

