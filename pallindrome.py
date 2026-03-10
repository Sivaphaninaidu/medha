num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10          # get last digit
    reverse = reverse * 10 + digit
    num = num // 10           # remove last digit

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")