# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is the same when read forward and backward.
# Example: madam, racecar

text = input("Enter a string: ").lower().replace(" ", "")

if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")