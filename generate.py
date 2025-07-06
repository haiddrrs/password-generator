# This script generates a random password based on user input.
import random
import string

# This asks the user about the required length and also validates the data.
length = int(input("Enter the length of the password: "))
if length < 1:
    print("Password must be atleast 1 character long .")
    exit()
elif length > 100:
    print("Password must be less than 100 characters.")
    exit()

symbols = input("Include symbols? (y/n): ")
numbers = input("Include numbers? (y/n): ")
uppercase = input("Include uppercase letters? (y/n): ")

lowercase = string.ascii_lowercase

if symbols == 'y':
   symbol_pool = string.punctuation
if numbers == 'y':
   number_pool = string.digits
if uppercase == 'y':
   upper_pool = string.ascii_uppercase

password = ''
while len(password) < length:
   password = password + random.choice(lowercase)
   password = password + random.choice(symbol_pool)
   password = password + random.choice(number_pool)
   password = password + random.choice(upper_pool)

print("Password: ", password)
