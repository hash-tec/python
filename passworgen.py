import random
print("Welcome to password generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letter_num = int(input("How many letters do you want in your password?\n"))
numbers_num = int(input("How numbers do you want in your password?\n"))
symbol_num = int(input("How many symbols do you want in your password?\n"))
password_list =[]
for alpha in range (letter_num):
    password_list.append(random.choice(letters))
for _ in range (numbers_num):
    password_list.append(random.choice(numbers))
for _ in range (symbol_num):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password =''
for char in password_list:
    password += char
print(f"Your password is {password}")

