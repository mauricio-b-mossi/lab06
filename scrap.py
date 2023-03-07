from ctypes import sizeof
from typing import List

print(12345 // 10**1)
print(12345 // 10**2)
print(12345 // 10**3)
print(12345 // 10**4)

def get_digits(num : int):
    size = len(str(num))
    digits = []
    for i in range(1, size):
        print(num // 10**i)

get_digits(12345)
