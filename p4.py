def palindrome(n):
	return str(n)==str(n)[::-1]
a=[]
for i in xrange(1000,0,-1):
	for j in xrange(1000,0,-1):
		if palindrome(i*j):
			a.append(i*j)
print max(a)		
