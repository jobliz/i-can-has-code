import math
from itertools import combinations

equals_int  = lambda n: math.modf(n)[0] == 0.0
hypothenuse = lambda a, b: (a**2 + b**2) ** 0.5

for comb in combinations(xrange(1, 1000), 2):
    a, b = comb[0], comb[1]
    c = hypothenuse(a, b)
    if equals_int(c):
        if a + b + int(c) == 1000:
            print int(a * b * c)
            break
