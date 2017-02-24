def is_prime(n):
	if n==1:
		return False
	for i in xrange(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

def is_trucatable(n):
	if is_prime(n):
		temp=str(n)
		for i in xrange(1,len(temp)):
			if not(is_prime(int(temp[:-i]))):
				return False
			if not(is_prime(int(temp[i:]))):
				return False
		return True
	#return False
sum1=0
for i in xrange(999999,10,-1):
	if is_trucatable(i):
		sum1+=i

print sum1