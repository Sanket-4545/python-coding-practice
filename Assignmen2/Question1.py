salary = float(input("Enter your salary:"))
if salary < 30000 :
  
    print("Based on you salary your tax is :" ,(salary*5)/100)
if salary > 30000 and salary <70000 :
    print("tax :" ,(salary*15)/100) 
if salary > 70000:
    print("tax :", (salary*25)/100)