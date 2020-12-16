import random

from validator.input_validator import InputValidator
from hint_checker import HintChecker
from enums.colours import Colours

class Mastermind:
    
    def __init__(self, input_validator: InputValidator, hint_checker: HintChecker):
        self.input_validator = input_validator
        self.hint_checker = hint_checker
    
    def initialise_secret_code(self):
        secret_code = []
        
        # four random colours
        for num in range(4):
            random_num = random.randint(1, len(Colours))
            secret_code.append(Colours(random_num))
            
        self.secret_code = secret_code
        

    def play():
        pass
    