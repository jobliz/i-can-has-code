# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 3 5 7 11 13 17 19

nums = range(1,21)
current = 20

while True:
	current += 1
	print current
	flag = True

	for n in nums:
		if (current % n != 0):
			flag = False
			break

	if flag == True:
		print current
		break
		
# 232792560, or was it? -.-
# dear god, it's SLOOOOOOOOOOOOOW
