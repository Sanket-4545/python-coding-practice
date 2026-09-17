# Q2. Take two numbers as input from the user and print their sum, difference, 
# product, and quotient. 

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("The sum of these two numbers is:", a + b)
print("The difference of these two numbers is:", a - b)
print("The product of these two numbers is:", a * b)

if b != 0:
    print("The quotient of these two numbers is:", a / b)
else:
    print("Quotient is not possible because division by zero is not allowed.")
