def ispal(n):
	s = str(n)
	l = len(s)	

	if (len(s) % 2 == 0):
		h = l / 2
	else:
		h = (n - 1) / 2

	d = s[:h]
	i = s[-h:][::-1]

	if d == i: return True	
	return False

from itertools import combinations

nums  = range(100, 1000)
combs = list(combinations(nums, 2))

top = 0
for c in combs:
	mult = c[0] * c[1]
	if (ispal(mult)) and (mult > top):
		top = mult
		print c, mult
