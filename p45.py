t,h,p=[],[],[]
for n in xrange(1,100000):
	t.append(n*(n+1)/2)
	p.append(n*(3*n-1)/2)
	h.append(n*(2*n-1))
print set(t).intersection(p).intersection(h)