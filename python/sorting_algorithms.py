# Sorting algorithm study in Python. Reference material:
# http://www.daniweb.com/software-development/python/code/216689/sorting-algorithms-in-python

# Insertion sort: https://en.wikipedia.org/wiki/Insertion_sort
# Linear check, pushing numbers to the right
def isort(a): # let's call it (a)rray
    for i in xrange(1, len(a)):
        save = a[i]
        j = i
        while j > 0 and a[j - 1] > save:  # start: list[j-1] > list[j]?
            a[j] = a[j - 1]               # pushes numbers to the right
            j -= 1                        # checking to the left decreased
        a[j] = save                       # stores save in current ok pos
                                          #   the last checked number appears
                                          #   twice and this puts save in the
                                          #   lesser position

# Selection sort: https://en.wikipedia.org/wiki/Selection_sort
# Linearly go to the right, swapping the current with the minimum found
# 1) Find the minimum value in the list
# 2) Swap it with the value in the first position
# 3) Repeat the steps above for the remainder of the list
#    (starting at the second position and advancing each time)
def ssort(a):
    for i in xrange(0, len(a)):
        minim = i                           # save the current position
        for j in xrange(i+1, len(a)):       # go through array from next pos
             if a[j] < a[minim]:            # if this is less than the current
                minim = j                   # this index is the new current
        a[minim], a[i] = a[i], a[minim]     # swap

test = [5,6,7,100,2,59,1]
# ssort(test)
# print test






















