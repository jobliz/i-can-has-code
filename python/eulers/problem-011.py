# Rationale for using an 1-dimensional list
#    * Each row contains 20 numbers
#    * 3 rows down is +60 from current index
#    * 3 rows up is -60 from current index
#    * left and right are just -1 or +1 to each side
#    * diagonals occur if a combination of vertical and horizontal happens,
#      adding or substracting multiples of 20 for vertical values
#      and the number of steps for horizontal values
#
#  This problem is still rather crude. I just made it more readable and
#  substituted the fugly lhp (list has position) function with a nicer lambda
#
#  On the past I decided to submit the results of each diagonal as I made them, 
#  it just happened that the first one got lucky. It's incomplete, and I'm sure
#  there is a general way to solve it, but I'm still fond of this approach =)
#
#  TODO: Find a general function to solve this class of problems!

base = [ int(n) for n in open('011_data.txt', 'r').read().split() ]
hasindex = lambda lst, index: index <= len(lst) - 1
possible = []

for i in xrange(0, len(base)):
    up, down, left, right = False, False, False, False

    if hasindex(base, i+60): 
        possible.append(base[i] * base[i+20] * base[i+40] * base[i+60]) 
        down = True
    
    if hasindex(base, i-60): 
        possible.append(base[i] * base[i-20] * base[i-40] * base[i-60]) 
        up = True
    
    if hasindex(base, i+3) : 
        possible.append(base[i] * base[i+1] * base[i+2] * base[i+3])
        right = True 
    
    if hasindex(base, i-3) : 
        possible.append(base[i] * base[i-1] * base[i-2] * base[i-3]) 
        left = True

    if ((up == True) and (left == True)): 
        possible.append(base[i] * base[i-19] * base[i-38] * base[i-57])

top = 0
for r in possible:
    if r > top: top = r

print top
