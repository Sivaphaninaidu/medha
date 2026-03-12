# Write a program that creates a nickname for a user based on their full name. It should:

# Ask for their first and last name

# Create a nickname using the first two letters of their first name and the first three letters of their last name

# Display the nickname in all uppercase



first_name = input("enter surname: ")
last_name = input("enter name: ")
nickname = first_name[0:2:]+last_name[0:3:]
b = nickname.upper()
print(nickname , b)
