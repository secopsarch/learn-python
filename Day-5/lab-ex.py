# lab exercise password generator

import random



letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+']

# deck = [letters, numbers, symbols]
# random.shuffle(deck)
# print(deck)

print("Welcome to Password Generator!")
a_letters = int(input("How many letters you like in your password?\n"))
a_symbols = int(input("How many symbols would you like?\n"))
a_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for l in range(a_letters):
    password_list.append(random.choice(letters))
for n in range(a_numbers):
    password_list.append(random.choice(numbers))
for s in range(a_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)
print(f"the password is: {password}")

    

