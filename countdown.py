def countdown(n):
	print "Count Down"
	while n > 0:
		yield n
		n -= 1

c = countdown(5)

#print c.next()
print c.next()
for i in c:
	print i
#c.previous