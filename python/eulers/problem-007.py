# check if number is prime
def isprime(n):
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True

# prime number generator
def prime_gen():
    yield 2; yield 3
    current = 3
    while True:
        current += 2
        if isprime(current):
            yield current

# nth result of a generator (preferably infinite as prime numbers)
def nth_gen(n, generator):
    gen = generator()
    current = 0
    while True:
        temp = gen.next()
        current += 1
        if current == n:
            return temp
        
print nth_gen(10001, prime_gen)
