def is_prime(n):
    for i in range(2,int(n**0.5+1)):
        if (n%i==0):
            return False
    return True
res=0
n=600851475143
for i in xrange(2,n):
	if n%i==0 and is_prime(i):
		res=i
		print i
#print res