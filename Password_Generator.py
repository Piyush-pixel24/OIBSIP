import string
import random

print("🔐 Password Generator 🔐")

length = int(input("Enter the password length: "))

use_letters = input("Do you want to Include letters? (y/n): ").lower() == 'y'
use_digits = input("Do you want to Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Do you want to Include symbols? (y/n): ").lower() == 'y'

characters = ""

if use_letters:
    characters += string.ascii_letters
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if characters == "":
    print(" You must select at least one option!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

print("✅ Generated Password:", password)