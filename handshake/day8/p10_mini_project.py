#Mini project: Student Management using OOP concepts.
class student:
    def __init__(self,roll,name,branch):
        self.roll=roll
        self.name=name
        self.branch=branch

class studentmanagment:
    def __init__(self):
        self.student=[]


    def add_student(self):
        roll= int(input("enter roll no:"))
        name= input("enter your name:")
        branch= input("enter your branch:")

        s=student(roll,name,branch)
        self.student.append(s)
        print("student added✅✅")

    def display_student(self):
        if len(self.student)==0:
            print("no student found")

        else:
            for s in self.student:
                print(s.roll,s.name,s.branch)

    def search_student(self):
        roll=input("enter roll number")
        found=False

        for s in self.student:
            if s.roll==roll:
                print("student found",s.roll,s.name,s.branch)
                found=True

        if not found:
            print("student not found")

    def delete_student(self):
        roll=input("enter roll number:")
        found=False

        for s in self.student:
            if s.roll==roll:
                self.remove.student(s)
                print("student deleted")
                found=True

        if not found:
            print("student not found")

obj=studentmanagment()

while True:
    print("/n1.add student")
    print("2.display student")
    print("3.search student")
    print("4.delete student")
    print("5.exit")


    choice=input("enter your choice:")

    if choice=="1":
        obj.add_student()

    elif choice=="2":
        obj.display_student()

    elif choice=="3":
        obj.search_student()
    elif choice=="4":
        obj.delete_student()

    elif choice=="5":
        print("program ended")
        break
    else:
        print("wrong input")

