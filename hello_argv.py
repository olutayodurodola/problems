import sys
if sys.argv[1] != "":
	print "hello " + sys.argv[1]

a ={}
a["the"] = 1
a["boy"] = 0
a["is"] = 2
a["the"] = 5

print a.keys()
print a.values()