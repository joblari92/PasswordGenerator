#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list_letters = []
list_symbols = []
list_numbers = []
for n in range(0,nr_letters):
    list_letters.append(letters[random.randint(0,len(letters)-1)])
print(list_letters)
for n in range(0,nr_symbols):
    list_symbols.append(symbols[random.randint(0,len(symbols)-1)])
print(list_symbols)
for n in range(0,nr_numbers):
    list_numbers.append(numbers[random.randint(0,len(numbers)-1)])
print(list_numbers)

list_password = []

list_password.append(list_letters)
list_password.append(list_numbers)
list_password.append(list_symbols)

print(list_password)