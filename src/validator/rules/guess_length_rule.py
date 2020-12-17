from enums.colours import Colours
from validator.rules.rule_interface import RuleInterface

from typing import List

class GuessLengthRule(RuleInterface):
    
    def is_valid(self, user_input: List):
        return len(user_input) == 4
    
    def error_message(self):
        return "user input is not the correct length, all guesses must be four colours!"
