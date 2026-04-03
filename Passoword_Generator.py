import random 
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'
print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like?\n'))
nr_numbers = int(input(f'How many numbers would you like?\n'))



easy_password = ''
for i in range(nr_letters):
    easy_password+=random.choice(letters)

for i in range(nr_symbols):
   easy_password+=random.choice(symbols)

for i in range(nr_numbers):
    easy_password+=random.choice(numbers)        

print(f"Your password is: {easy_password}")



password_list = []
for i in range(nr_letters):
    password_list +=random.choice(letters)

for i in range(nr_symbols):
    password_list +=random.choice(symbols)      

for i in range(nr_numbers):
    password_list +=random.choice(numbers)

random.shuffle(password_list)
password = ''
for char in password_list:
    password += char
  
print(f"Your password is: {password}")
