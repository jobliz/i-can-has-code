from itertools import combinations

ispal = lambda n: str(n) == str(n)[::-1]    # palindrome check
pairs = combinations(xrange(100, 1000), 2)  # three digit numbers in pairs

print max([p[0]*p[1] for p in pairs if ispal(p[0]*p[1])])



		
