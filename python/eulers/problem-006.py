sum_square = lambda n: sum([x**2 for x in xrange(1, n+1)])
square_sum = lambda n: sum(xrange(1, n+1)) ** 2

print (sum_square(100) - square_sum(100)) * -1
