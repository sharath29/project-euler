sum1=0
for i in xrange(10,9999999):
	res=0
	temp=str(i)
	for j in temp:
		res+=int(j)**5
	if res==i:
		sum1+=i
print sum1
