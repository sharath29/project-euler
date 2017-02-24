a=[1,2,5,10,20,50,100,200]
b=[0 for i in range(201)]
b[0]=1
for j in xrange(8):
	for i in xrange(1,201):
		if i-a[j]>=0:
			b[i]+=b[i-a[j]]
print b
