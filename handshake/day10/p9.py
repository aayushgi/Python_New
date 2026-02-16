#Combine iterators and generators in one code.
# Custom Iterator (Even Numbers)
class EvenIterator:
    def __init__(self, max_num):
        self.num = 0
        self.max = max_num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


# Generator (Square Numbers)
def square_generator(limit):
    for i in range(limit):
        yield i * i


print("Even numbers using Iterator:")
even_obj = EvenIterator(10)

for num in even_obj:
    print(num)

print("\nSquare numbers using Generator:")
for sq in square_generator(5):
    print(sq)
