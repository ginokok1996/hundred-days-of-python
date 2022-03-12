#Password Generator Project
import random

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+="

letter_list = list(letters);
numbers_list = list(numbers);
symbols_list = list(symbols);

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = "";
result = "";

for n in range(nr_letters):
    random.shuffle(letter_list)
    password += letter_list[n]
    
for n in range(nr_symbols):
    random.shuffle(symbols_list)
    password += symbols_list[n]
    
for n in range(nr_numbers):
    random.shuffle(numbers_list)
    password += numbers_list[n]


password = list(password)
random.shuffle(password)

result = result.join(password)

print(result)