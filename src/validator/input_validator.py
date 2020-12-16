from typing import List

from validator.rules.rule_interface import RuleInterface


class InputValidator:
    
    def __init__(self, rules: List[RuleInterface]):
        self.rules = rules
    
    def validate(self, user_input):
        for rule in self.rules:
            if not rule.is_valid(user_input):
                print(rule.error_message())
                return False

        return True
