#Demonstrate polymorphism with multiple classes.
class men:
    def relation(self):
        pass

class father(men):
    def relation(self):
        return "i am father here"
class hasband(men):
    def relation(self):
        return "i am hasband here"
class son(men):
    def relation(self):
        return "i am son here"
class boyfriend(men):
    def relation(self):
        return "i am boyfriend here"
    

mens=[father(),hasband(),son(),boyfriend()]
print("men as diffrent roles")
for men in mens:
    
    print(men.relation())