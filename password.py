from functools import reduce
from typing import Tuple

transform_values = {
        1 : 4,
        2 : 5,
        3 : 6,
        4 : 7,
        5 : 8,
        6 : 9,
        7 : 0,
        8 : 1,
        9 : 2
    }

def encode(password : str, inc : int = 3) -> Tuple[str, bool]:
    """
    Function accepts an 8 digit string of numbers, it will return a tuple 
    containing the encoded string and a boolean representing the success state.

    The encoding process will consist of iterating over each digit in the 
    password an performing an opration to it.

    - Overflows will be mod by 10 to return a single digit:
        . If digit 11 then 11 % 10 = 1.
    """

    if(len(password) != 8):
        return "", False
     
    try:
        i_password = int(password)
    except ValueError:
        print("Value Error: Cannot Convert Password to Int")
        return "", False

    digits = []

    #Loop gets all the digits and increments them by inc.
    for i in range(len(password)):
        #Getting single digit.
        digit = (i_password // 10**i % 10)
        #Appending digit plus inc mod 10 to avoid overflow.
        digits.append(str((digit + inc) % 10))

    digits.reverse()


    return reduce(lambda x, y : x + y, digits), True

def decode(password : str, inc : int = 3) -> Tuple[str, bool]:

    if(len(password) != 8):
        return "", False

    try:
        i_password = int(password)
    except ValueError:
        print("Value Error: Cannot Convert Password to Int")
        return "", False

    digits = []

    for i in range(len(password)):
        digit = (i_password // 10**i % 10)
        digits.append(str(abs(digit - inc)))

    digits.reverse()

    return reduce(lambda x, y : x + y, digits), True







