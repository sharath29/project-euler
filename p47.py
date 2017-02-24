def is_prime(n):
	for i in xrange(2,int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

def factors(n):
	a=[]
	for i in xrange(2,int(n**0.5)+1):
		if n%i == 0:
			if is_prime(i):
				a.append(i)
			if is_prime(n/i):
				a.append(n/i)
	return a


b=[]
for i in xrange(1000,1000000):
	b.append(len(factors(i)))


for i,j in enumerate(b):
	if j==4 and b[i+1]==4 and b[i+2]==4 and b[i+3]==4:
		print 1000+i
		break
