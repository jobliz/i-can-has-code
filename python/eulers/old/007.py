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

c = 1
num = 2

while c != 10001:
	c += 1
	num = nextprime(num)
	print c

print num
