# Password Generator Project
"""Write a program to generate password of given length.
Sample Input:
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
4
How many numbers would you like?
4
Sample Output:
Easy Password: Yavv*#&#1416
Hard Password: #v&641v*Y1#a"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
iter_object = None
letters_str, symbols_str, numbers_str = "", "", ""
if nr_letters >= nr_numbers and nr_letters >= nr_symbols:
  iter_object = nr_letters
elif nr_numbers >= nr_symbols:
  iter_object = nr_numbers
else:
  iter_object = nr_symbols
for i in range(0, iter_object):
  if i <= nr_letters - 1:
    letters_str += letters[random.randint(0, len(letters)-1)]
  if i <= nr_numbers - 1:
    numbers_str += numbers[random.randint(0, len(numbers)-1)]
  if i <= nr_symbols -1:
    symbols_str += symbols[random.randint(0, len(symbols)-1)]
easy_password = letters_str + symbols_str + numbers_str
print(f"Easy Password: {easy_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password, given_str = str(), easy_password
for i in range(len(given_str)):
    ch = given_str[random.randint(0, len(given_str)-1)]
    hard_password += ch
    given_str = given_str.replace(ch, '', 1)
    if not given_str:
        break
print(f"Hard Password: {hard_password}")
