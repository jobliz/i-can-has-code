# greatest common divisor
def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a

# least common multiple
def lcm(a, b):
    return (a * b) / (gcd(a, b))
    
print reduce(lcm, range(1, 21))
