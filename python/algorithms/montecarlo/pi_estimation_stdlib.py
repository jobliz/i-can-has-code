# This code is from http://niallohiggins.com/2007/07/05/monte-carlo-simulation-in-python-1/. From the post, for convenience:

"""Imagine a dart board inside of a square. If you throw darts, in a random fashion, at the square, counting the number of darts which land on the dart board versus the number which land on the square, you can approximate Pi with some simple arithmetic."""

from random import random
from math import pow, sqrt

DARTS=1000000
hits = 0
throws = 0
for i in range (1, DARTS):
    throws += 1
    x = random()
    y = random()
    dist = sqrt(pow(x, 2) + pow(y, 2))
    if dist <= 1.0:
        hits = hits + 1.0

# hits / throws = 1/4 Pi
pi = 4 * (hits / throws)

print "pi = %s" %(pi)
