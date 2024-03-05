#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for the number of letters, symbols, and numbers
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Count the number of elements in each list
num_letters = len(letters)
num_numbers = len(numbers)
num_symbols = len(symbols)

# Generate the password

password = ''
for _ in range(nr_letters):
    # Generate a random letter and add it to the password
    random_letter = letters[random.randint(0, num_letters - 1)]
    password += random_letter

for _ in range(nr_symbols):
    # Generate a random symbol and add it to the password
    random_symbol = symbols[random.randint(0, num_symbols - 1)]
    password += random_symbol

for _ in range(nr_numbers):
    # Generate a random number and add it to the password
    random_number = numbers[random.randint(0, num_numbers - 1)]
    password += random_number  

# Shuffle the password (optional)
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)

print(f"Your password is: {shuffled_password}")  



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P