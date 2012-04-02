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
			current = temp
	return primes

def allperms(l):
	sz = len(l)
	if sz <= 1:
		return [l]
	return [p[:i]+[l[0]]+p[i:] for i in xrange(sz) for p in allperms(l[1:])]

from itertools import combinations

def mycombs(l):
	length = len(l)
	result = []
	while(length != 0):
		lenset = combinations(l, length)
		result += lenset
		length -= 1
	return result

def myfind(n):
	primes  = [2]
	currentp = 2
	nextlist = []
	prevlist = primes
	top = 0
	
	while n > currentp:
		currentp = nextprime(primes[-1])
		primes.append(currentp)
		nextlist = mycombs(primes)

		#print prevlist
		temp = filter(lambda x:x not in prevlist, nextlist)
		for t in temp:
			allmult = reduce(lambda x, y: x*y, t)
				
			if (allmult == n):
				print ''
				print 'FOR ' + str(allmult) + ' MULTS ARE:'
				print t
				exit()
			print t, allmult
		prevlist = temp + filter(lambda x:x not in temp, nextlist)
		print ''

# ESTA ES LA FUNCION CORRECTA QUE HACE EL TRABAJO
def primestoward(n):
	primes = [2]
	myprimes = []
	old = []
	while True:
		temp = nextprime(primes[-1])
		primes.append(temp)
		allcombs = mycombs(myprimes)
		
		if temp < n:
			if (n % temp == 0):
				myprimes.append(temp)
		else:
			break

		if old != allcombs:
			print allcombs
			for c in allcombs:
				allmult = reduce(lambda x, y: x*y, c)
				print allmult, c
				if n == allmult:
					print 'I FOUND IT:'
					print c
					exit()
		
	return myprimes

rr = primestoward(600851475143)
		
# 42
#myfind(600851475143)

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

union = l1 + filter(lambda x:x not in l1, l2)
inter = filter(lambda x:x in l1, l2)
diff  = filter(lambda x:x not in l1, l2)

	
#x = primesbelow(600851475143)
#print x
	
