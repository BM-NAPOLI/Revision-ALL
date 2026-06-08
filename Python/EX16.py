x = str(input("Enter a string: "))

y = x[::-1]
if x == y:
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")