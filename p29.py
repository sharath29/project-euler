a=[]
for i in xrange(2,101):
	for x in xrange(2,101):
		a.append(i**x)

print len(list(set(a)))