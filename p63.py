count = 0

for n in xrange(1,100):
	for x in xrange(1,10):
		if 10**(n-1) <= x**n and x < 10**n:
			print x,
			count+=1
	print '\n'
print "count %d" % count

