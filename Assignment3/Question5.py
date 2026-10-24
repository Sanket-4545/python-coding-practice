# Q5.Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary:
# 1. A- Add a student
# 2. B- Update marks
# 3. C- Search for a student
# 4. D- Display all students and marks
dict = {
    "Sanket" : 45,
    "Dhanraj" : 33,
    "Tejas" : 46,
    "Rohit" : 50,
    "Naman" :49
}
print("A--> Add a student")
print("B--> Update marks")
print("C--> Search for a student")
print("D--> Display all students and marks")

Key = input("Enter Key:")

if Key.upper() == "A":
    name = input("Enter Studen Name :")
    mark = input("Enter Student Mark :")
    dict[name] = mark
    print(f"Student {name} Having added mark {mark}")

elif Key.upper() == "B":
    name = input("Enter Name :")
    mark = input("Enter Mark :")
    dict[name] = mark
    print(f"Student {name} Having updated mark {mark}")

elif Key.upper() == "C":
    name = input("Enter Studen Name :")
    if name in dict:
        print(f"Student {name} Having mark {dict[name]}")
    else:
        print(f"Student {name} not found.")

elif Key.upper() == "D":
    print("Student Name and Marks are :")
    for key, value in dict.items():
        print(f"{key} : {value}")
else:
    print("Invalid key ❌ . Choose A, B, C, or D.")