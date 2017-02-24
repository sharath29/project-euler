def factorial(n):
	return reduce(lambda x,y:x*y,[int(i) for i in xrange(n,1,-1)])

a=[]
a.append(1)
a.append(1)
for i in range(2,10):
	a.append(factorial(i))
res=0

for i in xrange(12,12000000):
	for k in str(i):
		res+=a[int(k)]
	if res==i:
		print i	
	res=0

