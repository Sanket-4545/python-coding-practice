info = [
    ("Sanket" ,"Maths"),
    ("Dhanraj" ,"Biology"),
    ("Manoj" ,"Maths"),
    ("Tejas" ,"English"),
    ("Sumit" ,"Biology"),
    ("Rahul" ,"Maths"),
    ("Manik" ,"English")
]
unique_courses = set()
unique_name = set()
for tup in info:
    print(tup)
    unique_courses.add(tup[1])
    unique_name.add(tup[0])
print(f"Unique courses are:{unique_courses}")
print(f"Unique name are:{unique_name}")
