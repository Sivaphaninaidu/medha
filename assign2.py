# Create a program that asks the user to enter a string, then displays:

# The string in all uppercase

# The string in all lowercase

# The length of the string

# The first and last characters

# The string reversed

name = input("enter your name: ")
a = name.upper()
b = name.lower()
c = len(name)
d = name[0:5:4]
e = name[::-1]
print(a,b,c,d,e)
