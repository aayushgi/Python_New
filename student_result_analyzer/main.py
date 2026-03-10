import json
import os
students=[]


def add_student():
    roll=input("enter roll number here: ")
    name=input("enter name here: ")
    class_name=input("enter class here: ")


    student={
        "roll":roll,
        "name":name,
        "class":class_name,
        "marks":{}
    }
    students.append(student)
    print("student added")

def enter_marks():
    roll=input("enter roll number here:")
    for s in students:
        if s.get("roll") == roll:
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


def list_students():
    for s in students:
        print("-------------------------------------------------------")
        print("roll number",s["roll"])
        print("name",s["name"])
        print("percentage:",s.get("percentage","not computed"))


def save_json():
    os.makedirs("data", exist_ok=True)

    with open("data/students.json", "w") as f:
        json.dump({"students": students}, f, indent=4)

    print("data saved")


def load_json():
    global students

    try:
        with open("data/students.json","r")as f:
            data=json.load(f)
            students=data["students"]
            print("data loaded")

    except FileNotFoundError:
        print("file not found")

while True:
    print("\n----- ---------------student result analyzer-----------------------")
    print("1 to add student")
    print("2 to enter marks")
    print("3 to compute result")
    print("4 to list students")
    print("5 to save json")
    print("6 to load json")
    print("0 for exit")


    choice=input("enter your choice")

    if choice=="1":
        add_student()
    elif choice=="2":
        enter_marks()

    elif choice=="3":
        compute_result()
    elif choice=="4":
        list_students()
    elif choice=="5":
        save_json()
    elif choice=="6":
        load_json()
    elif choice=="0":
        break


