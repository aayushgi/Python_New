
import json
import os
import datetime
import matplotlib.pyplot as plt

students=[]
def log_error(error_msg):
    base_dir = os.path.dirname(os.path.abspath(__file__))   
    file_path = os.path.join(base_dir, "error_log.txt")  
    with open("error_log.txt","a") as file:
        file.write(f"{datetime.datetime.now()}-{error_msg}\n")
def add_student():
    try:
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
    except Exception as e:
        print("error occurred in add_student")
        log_error(str(e))

def enter_marks():
    try:
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
    except Exception as e:
        print("error occured in enter_marks")
        log_error(str(e))
def compute_result():
    try:
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
    except Exception as e:
        print("error occured in compute_result")
        log_error(str(e))


def grade_distribution_chart():
    try:
        grade_count={
            "A+":0,
            "A":0,
            "B":0,
            "C":0,
            "D":0
        }
        for s in students:
            grade=s.get("grade")
            if grade:
                grade_count[grade]+=1

        grade=list(grade_count.keys())
        counts=list(grade_count.values())
        plt.bar(grade,counts)
        plt.title("Grade distributed chart")
        plt.xlabel("Grade")
        plt.ylabel("Number of students")
        plt.show()
    except Exception as e:
        print("error occured in grade distributed chart")
        log_error(str(e))
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
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(base_dir, "templates")
    os.makedirs(templates_dir, exist_ok=True)
    filename = os.path.join(templates_dir, f"report_{stu['roll']}.txt")
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
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        file_path = os.path.join(data_dir, "students.json")
        with open(file_path, "w") as f:
            json.dump({"students": students}, f, indent=4)
        print(f"data saved at: {file_path}")
    except Exception as e:
        print("error occured in compute_result")
        log_error(str(e))

def sort_students():
    if not students:
        print("no student avilable to sort")
        return
    print("enter 1 to sort by name")
    print("enter 2 to sort by roll number")
    choice = input("enter your choice ")
    if choice==1:
        students.sort(key=lambda x:x["name"].lower())
        print("students sorted by name")
    elif choice==2:
        students.sort(key=lambda x:x["roll"])
        print("students sorted by roll number")
    else:
        print("invalid input")

def load_json():
    
    global students
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "data")
        file_path = os.path.join(data_dir, "students.json")

        
        with open(file_path, "r") as f:
                data = json.load(f)
                students = data["students"]
                print("data loaded")

    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("error occured in load_json")
        log_error(str(e))

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
    print("11 to show grade distribution chart")
    print("12 to sort the students")
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
    elif choice=="11":
      grade_distribution_chart()

    elif choice=="12":
        sort_students()

    elif choice=="0":
        break


