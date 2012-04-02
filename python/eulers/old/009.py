def isqrt(n):
    xn = 1
    xn1 = (xn + n/xn)/2
    while abs(xn1 - xn) > 1:
        xn = xn1
        xn1 = (xn + n/xn)/2
    while xn1*xn1 > n:
        xn1 -= 1
    return xn1
    
def is_square(n): return isqrt(n)**2 == n

from itertools import combinations
from math import sqrt

nums  = range(1, 1000)
combs = list(combinations(nums, 2))
maybe = [ [x[0], x[1], sqrt((x[0]**2) + x[1]**2) ] for x in combs if is_square( (x[0]**2) + x[1]**2 )]
print maybe


for m in maybe:
	if (m[0] + m[1] + m[2]) == 1000:
		print m
		print m[0] * m[1] * m[2]
