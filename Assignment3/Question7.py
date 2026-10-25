# Q7.Write a program that takes a string from the user and prints the number of 
# spaces in the string.
 
string = input("Enter a string:")
count = 0 
for spaces in string:
    if spaces == " " :
        count += 1
print(f"Empty space in given string is : {count}")