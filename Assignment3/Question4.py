# Q4.Given a tuple of integers, 
# create:
# A tuple of all even numbers 
# A tuple of all odd numbers
tup = (1,2,3,4,5,6,7,8,9)
even_number = ()
odd_number = ()

for i in tup:
    if i % 2 == 0:
        even_number += (i,)
    else:
        odd_number +=(i,)

print(f"Even Number: {even_number}")
print(f"Odd Number: {odd_number}")

