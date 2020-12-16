from typing import List
import random

from src.enums.colours import Colours
from src.enums.hints import Hints




class HintChecker:
    
    def get_hints(self, user_input, secret_code):
        black_hints = self._get_black_hints(user_input, secret_code)
        white_hints = self._get_white_hints(user_input, secret_code)
        all_hints = black_hints + white_hints
        random.shuffle(all_hints)
        return all_hints


    def _get_white_hints(self, user_input, secret_code):
        hints = []

        for colour in user_input:
            if colour in secret_code:
                hints.append(Hints.White)
                secret_code.remove(colour)
                
        return hints
            
    
    def _get_black_hints(self, user_input: List[Colours], secret_code: List[Colours]) -> List[Hints]:
        hints = []
        
        for index, colour in enumerate(user_input):
            if colour == secret_code[index]:
                secret_code[index] = ''
                hints.append(Hints.Black)
                
        return hints
            
        
        
