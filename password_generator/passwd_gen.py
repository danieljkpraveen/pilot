import random
from utils import ltr, num, smb


def password_generator(letters, symbols, numbers):
    passwd = list()
    for char in range(letters):
        passwd.append(random.choice(ltr))
    for sym in range(symbols):
        passwd.append(random.choice(smb))
    for numb in range(numbers):
        passwd.append(random.choice(num))
    random.shuffle(passwd)
    password = ""
    for p in passwd:
        password += p
    return password

letters= int(input("Number of letters in password: ")) 
symbols = int(input(f"Number of symbols in password: "))
numbers = int(input(f"Number of integers in password: "))
password = password_generator(letters=letters, symbols=symbols, numbers=numbers)
print(f"Password generated: {password}")
