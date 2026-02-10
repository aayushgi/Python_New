#Create iterator printing even numbers up to 20.
class evenNumber:
    def __init__(self,max):

        self.max= max
        self.num=2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=self.max:
            value=self.num
            self.num+=2
            return value
        else:
            raise StopIteration
        

even=evenNumber(20)
for number in even:
    print(number)