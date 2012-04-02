# first attempt, years ago

serie = [1, 1]
total = 0
n = 0

while(n < 4000000):
	n = serie[-1] + serie[-2]
	serie.append(n)
	if (n % 2 == 0):
		total += n
	
print total
