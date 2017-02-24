def divisors_sum(n):
	divisors=[]
	for i in xrange(1,int(n**0.5)+1):
		if n%i==0:
			divisors.append((i,n/i));

	divisors=[sum(i) for i in divisors]
	return sum(divisors)-n
a=[]
for i in xrange(1,10000):
	k=divisors_sum(i)
	if(k!=i and divisors_sum(k)==i):
		a.append(i)
print a
print sum(a)