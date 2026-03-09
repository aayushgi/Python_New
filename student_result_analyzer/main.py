import json
students=[]


def add_student():
    roll=input("enter roll number here: ")
    name=input("enter name here: ")
    class_name=input("enter class here: ")


    student={
        "roll ":roll,
        "name ":name,
        "class ":class_name,
        "marks ":{}
    }
    students.append(student)
    print("student added")

def enter_marks():
    roll=input("enter roll number here:")
    for s in students:
        if s["roll"]==roll:
            subjects=["python","maths","DBMS","OS"]
            for sub in subjects:
                marks=int(input(f"enter marks for every {sub}: "))
                s["marks"][sub]=marks
            print("marks added")
            return
    print("student not found") 


def compute_result():
    for s in students:
        total=sum(s["marks"].values())
        percentage=total/len(s["marks"])   


        if percentage>=90:
            grade="A+"
        elif percentage>=80:
            grade="A"

        elif percentage>=70:
            grade="B+"
        elif percentage>=60:
            grade="B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        s["total"]=total
        s["percentage"]=percentage
        s["grade"]=grade
    print("result calculated")

    