# Q1. Write a program that takes as input. Using conditional statements, 
# calculate the final tax rate based on these rules: 
# • If salary < 30,000 → 5% 
# • If salary is 30,000–70,000 → 15% 
# • If salary > 70,000 → 25% 

Salary = int(input("Enter your salary"))

if Salary < 30000 :
    tax = (Salary / 100)* 5
    print("Your tax is :" , tax)

elif  Salary <= 70000:
    tax = tax = (Salary / 100)* 15
    print("Your tax is:" ,tax)

else:
    tax = tax = (Salary / 100)* 25
    print("Your tax is :", tax)