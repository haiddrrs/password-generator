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

chars = list(string.ascii_lowercase)
if symbols == 'y':
   chars = chars + list(string.punctuation)
if numbers == 'y':
   chars = chars + list(string.digits)
if uppercase == 'y':
   chars = chars + list(string.ascii_uppercase)

password = ''
for i in range(length):
   password = password + random.choice(chars)
print("Password: ", password)
