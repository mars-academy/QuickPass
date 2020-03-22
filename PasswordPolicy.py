class PasswordPolicy:
    def __init__(self, length: int = 16, contain_upper: bool = True, contain_lower: bool = True,
                 contain_number: bool = True,
                 contain_symbol: bool = True):
        self.length = length
        self.contain_upper = contain_upper
        self.contain_lower = contain_lower
        self.contain_number = contain_number
        self.contain_symbol = contain_symbol
