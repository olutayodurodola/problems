import sys

mylist = [10,-12,-69,-2,56,-100,-3,1]

maxneg = sys.maxsize * -1



for i in mylist:
	if i<0:
		if maxneg <= i:
			maxneg = i
		else:
			maxneg = maxneg
	else:
		pass
if maxneg == (sys.maxsize * -1):
	print "No negative number in list"
else:
	print maxneg
