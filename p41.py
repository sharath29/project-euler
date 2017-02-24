import itertools as yo
def is_prime(n):
	for i in xrange(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

for i in xrange(5,10):
	a=range(1,i)
	b=list(yo.permutations(a))
	for j in b:
		l=''.join(str(k) for k in j)
		if is_prime(int(l)):
			print l