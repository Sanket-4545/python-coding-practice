info = [
    ("Sanket" ,"Maths"),
    ("Dhanraj" ,"Biology"),
    ("Manoj" ,"Maths"),
    ("Tejas" ,"English"),
    ("Sumit" ,"Biology"),
    ("Rahul" ,"Maths"),
    ("Manik" ,"English")
]
# list all unique courses and name
courses_set = set()
unique_name = set()
for tup in info:
    print(tup)
    courses_set.add(tup[1])
    unique_name.add(tup[0])
print(f"Unique courses are:{courses_set}")
print(f"Unique name are:{unique_name}")

# list Student enrolled in english
for name , course in info:
    if(course == "English"):
        print(name)

  

