def generateSeries(n):
	if type(n) != int:
		return -1
	if type(n) == float:
		return -1
	if n < 0:
		return -1
	f0 = 0
	f1 = 1
	fseries = [0]
	while (n > 0):
		fseries.append(f1)
		f2 = f1 + f0
		f0 = f1
		f1 = f2
		n -= 1
	return fseries

print generateSeries(5)


def generateSeriesSum(n,radix=None):
	pass
	