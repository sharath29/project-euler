def never_palindrome(n):
	count = 0
	temp = str(n)
	while(temp != temp[::-1] or count == 0):
		temp = int(temp) + int(temp[::-1])
		count += 1
		if count == 50:
			return True
		temp = str(temp)
	return False

flag=0

for i in xrange(1,10001):
	if never_palindrome(i):
		flag+=1

print flag
