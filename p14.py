
max1=0
for i in xrange(10,837800):
	j=1
	x=i
	while x!=1:
		if x%2==0:
			x=x/2
			j+=1  
		else:
			x=(3*x)+1
			j+=1
	if max1<j:
		max1=j
		a=i
print max1,a