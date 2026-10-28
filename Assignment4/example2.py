#Constructor
class Student:
    def __init__(self , name , cgpa,dept ,Address):
        self.Address = Address
        self.name = name
        self.cgpa = cgpa
        self.dept = dept

stu1 = Student("Sanket" , 9.00 , "CSE" ,"Phandharpur")
print(stu1.name,stu1.cgpa,stu1.dept)

stu2 = Student("Dhanraj" , 9, "Agri","Kolhapur")
print(stu2.name)