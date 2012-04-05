def lhp(l, pos):
	""" Checks if given list has a position 'pos' """
	try:
		dummy = l[pos]
		return True
	except IndexError:
		return False

base = open('011_data.txt', 'r').read().split()
base = [ int(n) for n in base ]

res = []
for pos, item in enumerate(base):
	u = False
	d = False
	l = False
	r = False

	if lhp(base, pos + 60): res.append(base[pos] * base[pos + 20] * base[pos + 40] * base[pos + 60]); d = True # down
	if lhp(base, pos - 60): res.append(base[pos] * base[pos - 20] * base[pos - 40] * base[pos - 60]); u = True # up
	if lhp(base, pos + 3) : res.append(base[pos] * base[pos +  1] * base[pos +  2] * base[pos +  3]); r = True # right
	if lhp(base, pos - 3) : res.append(base[pos] * base[pos -  1] * base[pos -  2] * base[pos -  3]); l = True # left

	if ((u == True) and (l == True)): res.append(base[pos] * base[pos - 19] * base[pos - 38] * base[pos - 57])

top = 0
for r in res:
	if r > top: top = r

print top
