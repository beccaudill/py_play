'''
Masking all but the last 4 digits of a credit card number.

Highlights the use of:
1. Regular Expression library
2. Built-in map function

1/15/2024, Rebecca Caudill
'''

import re

# Prompt user to input a credit card number.
def inputPrompt():
    print("Please enter your credit card number:")
    ccNumberInput = input()
    maskCreditCard(ccNumberInput)   

# Count the number of digits in the user input;
# the sum function will add 1 for each true returned by isdigit.
# If input is invalid, prompt user to retry.
def maskCreditCard(ccNumber):
    ccNumberCount = sum(map(str.isdigit, ccNumber))

    if ccNumberCount == 16:
        x = re.sub("\d","*",ccNumber[0:12])
        print("Masked credit card number:")
        print(x + ccNumber[12:])
    else:
        print('Credit number is invalid. Please retry.')
        inputPrompt()

inputPrompt()
