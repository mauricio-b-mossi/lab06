import password as pw

def main():

    curr = ""
    
    print('-------------')
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

    while True:
        option = input("Please enter an option: ")

        if (option == "1"):
            password = input("Please enter your password to encode: ")
            curr, success = pw.encode(password)
            if success:
                print("Your password has been encoded and stored")
            else:
                print("Your password failed to encode")

        if(option == "2"):
            temp = curr
            curr, success = pw.decode(curr)
            if success:
                print(f"The encoded_password is {temp}, and the original \
                        password is {curr}")
            else:
                print(f"Failed to decode password")
                curr = temp

        if(option ==  "3"):
            break
                





if __name__ == '__main__':
    main()
