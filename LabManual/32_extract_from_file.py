# Q32. Write a python program to retrieve name and date of birth (mm-dd-yyyy) of students from a given file student.txt. 

def show_students(filePath):
    students = {}
    with open(filePath, "r") as file:
        for line in file:
            name, dob = line.split(", ")
            students[name] = dob[:-1]
        return students


data = show_students("student.txt")
print(data)
