#Hard level of Random Password Generator
# Easy level password generator
import random

print("Welcome to Password Generator")
nr_letters = int(input("How many letters would you like in Password ? "))
nr_numbers = int(input("How many numbers do you want in Password ? "))
nr_symbols = int(input("How many symbols do you want in Password ? "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 0]
symbols = ['!', '@', '$', '#', '^', '&', '*', '+', '(', ')']
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)

password = ""
for j in password_list:
    password += str(j)
print(password)
