from collections import Counter

ispal = lambda n: str(n) == str(n)[::-1] # palindrome check
revad = lambda n: n + int(str(n)[::-1])  # reverse and add

def lych_test(n, limit=50):
    count = 0
    for x in xrange(limit):
        n = revad(n)
        count += 1
        if ispal(n):
            return False, count
    return True, count

assert lych_test(47) == (False, 1)
assert lych_test(349) == (False, 3)
assert lych_test(10677, limit=60) == (False, 53) 
assert lych_test(4994) == (True, 50)
assert lych_test(196) == (True, 50)

print Counter([lych_test(x)[0] for x in xrange(10000)])
