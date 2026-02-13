#Write generator yielding square of numbers.
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

# Using the generator
gen = square_generator(5)

for value in gen:
    print(value)
