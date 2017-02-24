a=[]
for n in xrange(1,10000):
	a.append(n*(3*n-1)/2)

def is_pentagonal(n):
	l=int(((n*2)/3)**0.5)+1
	if n==l*(3*l-1)/2:
		return True
	else:
		return False

for i,j in enumerate(a):
	for k in xrange(i-1,-1,-1):
		if is_pentagonal(j+a[k]) and is_pentagonal(j-a[k]):
			print "sdafasfasresult=%d",j,a[k]
