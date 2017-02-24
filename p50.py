def is_prime(n):
    for i in range(2,int(n**0.5+1)):
        if (n%i==0):
            return False
    return True

a=[]
for i in range(2,1000):
	if is_prime(i):
		a.append(i)
b=[]
print a
for i in xrange(1,len(a)):
	b.append(sum(a[:i]))

for i in b[::-1]:
	if is_prime(i):
		print i

