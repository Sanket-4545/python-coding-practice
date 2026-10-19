# Q5. Write a function to return the sum of digits of a number, n.

def Sum_of_ditit(n):
    if n < 0:
        n = -n
    if n == 0:
        return 0

    sum = 0
    while n > 0:
        ditit = n % 10
        sum = sum + ditit
        n = n //10

    return sum

n = 1243
print(Sum_of_ditit(n))

