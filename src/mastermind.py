import random
import re

from enums.hints import Hints
from validator.input_validator import InputValidator
from hint_checker import HintChecker
from enums.colours import Colours


class Mastermind:

    def __init__(self, input_validator: InputValidator, hint_checker: HintChecker):
        self.input_validator = input_validator
        self.hint_checker = hint_checker

    def play(self):
        print("Welcome to mastermind, try and guess the secret code!")
        self._initialise_secret_code()
        
        guesses = 0

        while guesses < 60:
            print(f"This is guess number {guesses}:")
            print(f"valid colours to guess are: ")
            print("Red  Blue  Green  Orange  Purple  Yellow")

            user_input = input("Enter your guess: ")
            parsed_input = re.split("\s|,", user_input)
            
            print(parsed_input)

            if self.input_validator.validate(parsed_input):
                hints = self.hint_checker.get_hints(parsed_input, self.secret_code)
                print("HINTS: \n")
                print(hints)
                
                if hints.count(Hints.Black) == 4:
                    print("You WON!")
                    return

            guesses += 1
    
                

    def _initialise_secret_code(self):
        secret_code = []

        # four random colours
        for num in range(4):
            random_num = random.randint(1, len(Colours))
            secret_code.append(Colours(random_num))

        self.secret_code = secret_code
