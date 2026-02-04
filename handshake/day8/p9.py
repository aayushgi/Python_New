
#Create Vehicle, Car, and ElectricCar hierarchy.
class vehical:
    def start(self):
        print("vehical is starting")
class car(vehical):
    def drive(self):
        print("car is driving")
class electriccar(car):
    def charging(self):
        print("car is charging")
e=electriccar()
e.start()
e.drive()
e.charging()