def decoder(password : str) -> str:
    pass

def encoder(password : str):
    if(len(password) != 8):
        return ""
    i_password = int(password)

    digits = []

    power = 10

    index = 1

    while(index < 9):
        number = (i_password // 10**(index-1)) % 10**index 
        digits.append(number)
        index += 1

    return digits

print(encoder("12345678"))
