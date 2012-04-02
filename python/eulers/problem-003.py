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

# prime factorization
def prime_facts(n):
    factors = []
    primes = prime_gen()
    while True:
        prime = primes.next()
        if n % prime == 0:
            factors.append(prime)
            n = n / prime
        if n == 1:
            break
    return factors

print prime_facts(600851475143)[-1:][0]
