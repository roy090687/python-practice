import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '@']

print("Welcome to password generation!")

n_letters = int(input("How many letters you want for your password?\n"))
n_numbers = int(input("How many numbers you want for your password?\n"))
n_symbols = int(input("How many symbols you want for your password?\n"))

password_list = []
password = ""

for i in range(n_letters):
    ch = random.choice(letters)
    password_list.append(ch)

for i in range(n_numbers):
    ch = random.choice(numbers)
    password_list.append(ch)

for i in range(n_symbols):
    ch = random.choice(symbols)
    password_list.append(ch)

random.shuffle(password_list)

print("Password is: ")
for i in range(len(password_list)):
    password += password_list[i]

print(password)
