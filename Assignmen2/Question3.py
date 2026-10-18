# Q3. Write a function that prints the digits of a number, . 
# For eg:n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them. 


def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n // 10

n = 312
print_digits(n)

