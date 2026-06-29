import random
import string

print("===== PASSWORD GENERATOR =====")

# User Input
length = int(input("Enter the desired password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate Password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display Password
print("\nGenerated Password:")
print(password)