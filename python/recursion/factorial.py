import sys
sys.setrecursionlimit(2000)

def factorial(n):
    if n == 0:
        return 1
    else:
        temp = factorial(n - 1)
        print n, temp
        return n * temp

print factorial(4)
