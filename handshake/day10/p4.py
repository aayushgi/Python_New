
#Build generator for prime numbers up to 50.
def prime_generator(limit):
    for num in range(2,limit+1):
        is_prime=True


        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime= False
                break

        if is_prime:
            yield num


for prime in prime_generator(50):
    print(prime)