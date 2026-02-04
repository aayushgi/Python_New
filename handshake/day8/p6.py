#Show method overriding with same method name
class animal:
    def sound(self):
        print("animal makes sound")

class cat(animal):
    def sound(self):
        print("cat meaws")

c=cat()
c.sound()