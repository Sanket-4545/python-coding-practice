a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
def Find_Avg(a, b , c):
    avg = (a + b + c) / 3
    return avg

average = Find_Avg(a, b, c)
print("The average of the three numbers is:", average)