

def circular_shift(n):
	temp=str(n)
	k=len(temp)-1
	l=k
	res=int(temp[k])*(10**l)
	l=l-1
	for i in xrange(k):
		res+=int(temp[i])*(10**l)
		l-=1
	return res

def is_prime(n):
    for i in range(2,int(n**0.5+1)):
        if (n%i==0):
            return False
    return True
a=[]
for i in xrange(2,1000000):
	if is_prime(i):
		a.append(i)
b=[]
for i in a:
	l=0
	temp=len(str(i))
	k=i
	for j in xrange(temp):
		k=circular_shift(k)
		print 'this %d-%d',k,i
		if is_prime(k):
			l+=1
	if l==temp:
		b.append(i)
print b
	