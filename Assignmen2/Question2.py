 
# Q2. Write a function that takes two integers and and prints all even 
# numbers between them (inclusive). 

def print_even_number (start ,end):
    for i in range(start , end + 1):
        if i % 2 == 0:
            print(i)
print_even_number(10, 20)