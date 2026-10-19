# Q4. Write a function to return the count the number of digits in a number, n:
def find_count(n):

    if n < 0:
        n = -n
    if n == 0:
        return 1

    count = 0
    while n > 0:
        count = count + 1
        n = n // 10

    return count


n = 3123434
print(find_count(n))

