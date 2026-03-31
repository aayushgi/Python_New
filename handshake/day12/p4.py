#Create export_report_card(stu) for text file output
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


def search_by_grade(grade):
    found=False
    for s in students:
        if s.get("grade")==grade:
            print("---------------------------------------------------")
            print("roll number",s["roll"])
            print("name",s["name"])
            print("grade",s.get("grade"))
            print("percentage",s.get("percentage"))
            found=True
    if not found:
        print("no student with this grade")


def subject_topper_report():
    subjects=["python","maths","DBMS","OS"]
    for sub in subjects:
        topper=max(students,key=lambda s:s["marks"].get(sub,0))
        print("-----------------------------------------------------------")
        print(sub,"topper")
        print("name: ",topper["name"])
        print("marks",topper["marks"].get(sub,0))

def export_report_card(stu):
    filename=f"report_{stu['roll']}.txt"
    with open(filename,"w") as file:
        file.write("===========STUDENT REPORT CARD============\n\n")
        file.write(f"roll no. :{stu['roll']}\n")
        file.write(f"name :{stu['name']}\n")
        file.write(f"class :{stu['class']}\n\n")

        file.write("-----------marks-------------")

        total=0
        count = 0
        
        for subject, marks in stu["marks"].items():
            file.write(f"{subject}: {marks}\n")
            total += marks
            count += 1
        
        
        avg = total / count if count > 0 else 0
        
        file.write("\n-----------------\n")
        file.write(f"Total Marks : {total}\n")
        file.write(f"Average     : {avg:.2f}\n")
        
        
        if avg >= 90:
            grade = "A+"
        elif avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "F"
        
        file.write(f"Grade       : {grade}\n")
    
    print(f"Report card exported successfully to {filename}")

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

def delete_student():
    roll=input("enter roll number you want delete")
    for s in students:
        if s.get("roll")==roll:
            students.remove(s)
            print("student removed successfully")
            return
    print("student not found")

while True:
    print("\n----- ---------------student result analyzer-----------------------")
    print("1 to add student")
    print("2 to enter marks")
    print("3 to compute result")
    print("4 to list students")
    print("5 to save json")
    print("6 to load json")
    print("7 to delete student")
    print("8 to find student with their grade")
    print("9 to get subject topper list")
    print("10 to export report card")
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
    elif choice=="7":
        delete_student()
    elif choice=="8":
        grade=(input("enter the grade here"))
        search_by_grade(grade)
    elif choice=="9":
        subject_topper_report()
    elif choice=="10":
        roll = input("Enter roll number: ")
        for s in students:
            if s["roll"] == roll:
                export_report_card(s)
                break
        else:
            print("Student not found")
    elif choice=="0":
        break


