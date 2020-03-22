import random

from PasswordPolicy import PasswordPolicy


class PasswordBuilder:
    upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                  "T", "U", "V", "W", "X", "Y", "Z"]
    lower_case = [a.lower() for a in upper_case]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    allowed_chars = []

    def __init__(self, password_policy: PasswordPolicy = PasswordPolicy()):
        self.password_policy = password_policy

    def _make_char_set(self) -> None:
        allowed_chars = []
        if self.password_policy.contain_upper:
            allowed_chars += self.upper_case
        if self.password_policy.contain_lower:
            allowed_chars += self.lower_case
        if self.password_policy.contain_number:
            allowed_chars += self.numbers
        if self.password_policy.contain_symbol:
            allowed_chars += self.symbols
        self.allowed_chars = allowed_chars

    def _make_password(self) -> str:
        password = ""
        for i in range(self.password_policy.length):
            password += random.choice(self.allowed_chars)
        return password

    def build(self) -> str:
        """ Use this to make a new password """
        self._make_char_set()
        return self._make_password()
