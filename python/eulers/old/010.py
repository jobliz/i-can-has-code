def isprime(n):
	for x in range(2, int(n**0.5)+1):
		if n % x == 0:
			return False
	return True

def nextprime(n):
	x = n
	while True:
		x += 1
		if isprime(x):
			return x

def prevprime(n):
	x = n
	while True:
		x -= 1
		if ((x == 1) or (x == 0) ):
			return False
		if isprime(x):
			return x

def primesbelow(n):
	current = prevprime(n)
	primes  = [current]
	print current
	while(True):
		temp = prevprime(current)
		if temp == False:
			break
		else:
			primes.append(temp)
			print temp
			current = temp
	return primes


b2m = primesbelow(2000000)
print ""
print reduce(lambda x, y: x+y, b2m)

