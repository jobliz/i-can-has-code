# generic fibonacci number generator
def fib_gen():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

# limited fibonacci generator using previous one
def fib_limit(n):
    fibs = fib_gen()
    current = fibs.next()
    while current < n:
        yield current
        current = fibs.next()

print sum([ f for f in fib_limit(4000000) if f % 2 == 0 ])
