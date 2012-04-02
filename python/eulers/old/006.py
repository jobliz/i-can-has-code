def prob6(n):
	nums = range(1, (n + 1))
	sotq = reduce(lambda x, y: x+y, [x**2 for x in nums])
	sots = (reduce(lambda x, y: x+y, nums)) ** 2
	return (sotq - sots) * -1

print prob6(100)
