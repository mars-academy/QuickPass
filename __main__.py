from PasswordBuilder import PasswordBuilder
from PasswordPolicy import PasswordPolicy

if __name__ == '__main__':
    print("Hello, Welcome to QuickPass Password Generator.\nLet's generate a perfect password for you.")
    length = int(input("how many letter should it be? "))
    contain_upper_case = (input("Should I include uppercase letters? (y/n): ")[0].lower() == "y")
    contain_lower_case = (input("Should I include lowercase letters? (y/n): ")[0].lower() == "y")
    contain_numbers = (input("Should I include numbers? (y/n): ")[0].lower() == "y")
    contain_symbols = (input("Should I include symbols? (y/n): ")[0].lower() == "y")

    pass_policy = PasswordPolicy(length, contain_upper_case, contain_lower_case, contain_numbers, contain_symbols)
    pass_builder = PasswordBuilder(pass_policy)

    print("Done. Your password is: ", pass_builder.build())
