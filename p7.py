def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: 
            return False
    return True
a=[]
k=0
for i in xrange(2,10000000):
	if isPrime(i):
		a.append(i)
		k+=1
		if k==10001:
			print i
			exit()