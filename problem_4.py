def generateSeries(n):
	if type(n) != int:
		return -1
	if type(n) == float:
		return -1
	if n < 0:
		return -1
	f0 = 0
	f1 = 1
	fseries = []
	while (n > 0):
		fseries.append(f0)
		fseries.append(f1)
		f0 = f1
		f1 = f1 + f0
		n -= 1
	return fseries




def generateSeriesSum(n,radix=None):
	pass
	