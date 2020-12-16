from validator.rules.rule_interface import RuleInterface
from enums.colours import Colours

from typing import List



class ValidColour(RuleInterface):

    def is_valid(self, user_input: List[Colours]):
        for colour in user_input:
            if not colour in Colours.__members__:
                self.invalid_colour = colour
                return False
        return True
    
    def error_message(self):
        return f"user input is not correct, {self.invalid_colour} is not a valid colour!"
