# Q2.Given a list of integers compute the average of all numbers in the list.

list = [2,3,5,7,9]
total = 0
count =0
for value in list:
    total += value
    count += 1

print(f"The average is {total/count}")
print(f"there are {count} number of  integers are present in our list")    