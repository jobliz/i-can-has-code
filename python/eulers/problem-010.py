# erath is http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# mod 2, 3, 5 elimination and square upper limit from
# http://en.wikipedia.org/wiki/Sieve_of_Atkin
# TODO: Atkin's sieve

def erath(limit):
    check = lambda n: n % 2 != 0 and n % 3 != 0 and n % 5 != 0
    sieve = [n for n in xrange(1, limit) if check(n)][1:]
    primes = [2, 3, 5]
    
    while primes[-1] <= limit ** 0.5:
        primes.append(sieve[0])
        sieve = [ n for n in sieve if n % primes[-1] != 0 ]

    return primes + sieve

print sum(erath(2000000))
