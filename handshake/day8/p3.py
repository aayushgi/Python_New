
#Demonstrate private variables and getters/setters.
class student:
    def __init__(self,name,marks):
        self.name=name
        self._marks=marks


    def get_marks(self):
        return self._marks
    def set_marks(self,marks):
        self._marks=marks

s1=student("ayush",76)
print("marks",s1.get_marks())
s1.set_marks(45)
print("new marks",s1.get_marks())
