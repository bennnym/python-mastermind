from enums.colours import Colours

from typing import List


class RuleInterface:
    
    def is_valid(self, user_input: List[Colours]):
        """Check if input meets rule criteria"""
        pass
    
    def error_message(self):
        """returns error message"""
        pass
    
    