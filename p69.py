def is_prime(n):
    for i in range(2,int(n**0.5+1)):
        if (n%i==0):
            return False
    return True
def factors(n):	
	a=set()
	for i in xrange(1,int(n**0.5)+1):
		if n%i==0:
			a |= set([i,n/i])
	a.remove(1)
	return list(a)
def prime_factors(n):
	b=[]
	a = factors(n)
	for i in a:
		if is_prime(i):
			b.append(i)
	return b
def toient(n):
	a = prime_factors(n)
	res = n
	for i in a:
		res *= (1-1.0/i)
	return res

c=[]

for i in xrange(2,1000001):
	c.append([i,(i/toient(i))])

for i in c:
	print i
maxim = c[0][1]
for i in c:
	if maxim < i[1]:
		maxim = i[1]
		n = i[0]
print n,maxim
