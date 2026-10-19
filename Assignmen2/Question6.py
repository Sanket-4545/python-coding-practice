# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 
# and 5. 
def Print_divisible_number(n):
    for i in range(1, n + 1):
        if i  % 3 == 0 and i % 5 == 0:
            print(i)

print(Print_divisible_number(100))