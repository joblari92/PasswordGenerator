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
for n in range(0,nr_symbols):
    list_symbols.append(symbols[random.randint(0,len(symbols)-1)])
for n in range(0,nr_numbers):
    list_numbers.append(numbers[random.randint(0,len(numbers)-1)])

list_password = []

list_password.append(list_letters)
list_password.append(list_numbers)
list_password.append(list_symbols)

password = ''

while list_password != [[],[],[]]:
    rand_list = random.randint(0,len(list_password)-1)
    if rand_list == 0 and list_letters != []:
        rand_letter = random.randint(0,len(list_letters)-1)
        password += list_password[rand_list][rand_letter]
        list_letters.pop(rand_letter)
    elif rand_list == 1 and list_numbers != []:
        rand_number = random.randint(0, len(list_numbers) - 1)
        password += list_password[rand_list][rand_number]
        list_numbers.pop(rand_number)
    elif rand_list == 2 and list_symbols != []:
        rand_symbol = random.randint(0, len(list_symbols) - 1)
        password += list_password[rand_list][rand_symbol]
        list_symbols.pop(rand_symbol)

print(password)
