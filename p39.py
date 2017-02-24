from collections import Counter
a=[]
for i in xrange(10,1001):
	for j in xrange(1,int(i*(2**0.5))+1):
		for k in xrange(1,int(i*(2**0.5))+1):
			c= (j**2 + k**2)**0.5
			if j+k+c==i:
				a.append(i)
 print list(Counter(a))


