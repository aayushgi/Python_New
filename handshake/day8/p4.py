#Implement single inheritance using Teacher and Student.
class teacher:
    def show_teacher(self):
        print("this is teacher class")

class student(teacher):
    def show_student(self):
        print("this is student class")

s1=student()
s1.show_student()
s1.show_teacher()