# https://en.wikipedia.org/wiki/Wilson%27s_theorem

mult        = lambda a, b: a * b
factorial   = lambda n: reduce(mult, xrange(1, n+1)) # defined for n > 1
wilsonprime = lambda n: (factorial(n-1) + 1) % n == 0

for x in xrange(2, 100):
    if wilsonprime(x):
        print x
