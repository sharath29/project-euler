def is_palindrome(n):
	temp=str(n)
	if temp[::]==temp[::-1]:
		if bin(n)[2::]==bin(n)[2::][::-1]:
			return True
	else:
		return False
a=[]
for i in xrange(1,1000000):
	if is_palindrome(i):
		a.append(i)
print a
print sum(a)