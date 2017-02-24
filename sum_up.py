n=int(raw_input())
count=0
for i in xrange(1,n+1):
	if i%3==0 or i%5==0:
		count+=i
print count