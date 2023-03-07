from typing import Tuple
from functools import reduce


def encoder(password : str) -> str:
    #Checking if password is not 8 digits in len.
    if (len(password) != 8):
        return ""

    #Casting psw to int
    i_password = int(password)

    #Empty array to hold incremented digits
    digits = []

    for i in range(len(password)):
        #Getting all di
        digits.append(str(((i_password // 10**i) % 10) + 3))

    digits.reverse()

    return ''.join(digits)

def decoder(encoded_password : str) -> Tuple[str, bool]:
    pass

def main():

    password = ""
    encoded_password = ""

    print('-------------')
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    while True:
        option = input("Please enter an option: ")

        if (option == "1"):
            password = input("Please enter your password to encode: ")
            encoded_password, success = encoder(password)
            if success:
                print("Your password has been encoded and stored")
            else:
                print("Your password failed to encode")

        if(option == "2"):
            temp_pass, success = decoder(encoded_password)
            if success:
                print(f"The encoded_password is {encoded_password}, and the original \
                        password is {temp_pass}")
            else:
                print(f"Failed to decode password")

        if(option ==  "3"):
            break
                





if __name__ == '__main__':
    main()
