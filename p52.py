def check(a,b,c,d,e,f):
	l=set(sorted(list(a))).intersection(set(list(b))).intersection(set(list(c))).intersection(set(list(d))).intersection(set(list(e))).intersection(set(list(f)))
	k=set(sorted(list(a)))
	
	if l==k and (len(a)==len(b)==len(c)==len(d)==len(e)==len(f)):
		return True

for i in xrange(100,999999):
	if check(str(i),str(2*i),str(3*i),str(4*i),str(5*i),str(6*i)):
		print i
