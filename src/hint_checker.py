from typing import List
import random

from enums.colours import Colours
from enums.hints import Hints




class HintChecker:
    
    def get_hint(self, user_input, secret_code):
        black_hints = self._get_black_hints(user_input, secret_code)
        white_hints = self._get_white_hints(user_input, secret_code)
        all_hints = black_hints + white_hints
        return random.shuffle(all_hints)


    def _get_white_hints(self, user_input, secret_code):
        hints = []

        for colour, index in enumerate(user_input):
            if colour == secret_code[index]:
                secret_code.pop(index)
            
            if colour in secret_code:
                hints.append(Hints.White)
                secret_code.remove(colour)
                
        return hints
            
    
    def _get_black_hints(self, user_input: List[Colours], secret_code: List[Colours]) -> List[Hints]:
        hints = []
        
        for colour, index in enumerate(user_input):
            if colour == secret_code[index]:
                hints.append(Hints.Black)
                
        return hints
            
        
        
