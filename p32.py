def check(n):
	a=[0 for i in xrange(10)]
	for i in n:
		if a[int(i)]==0:
			a[int(i)]=1
		else:
			return False
	for j in xrange(1,10):
		if a[j]==0:
			return False
	if a[0]==1:
		return False
	
	return True

def factors(n):
	b=list((i,n/i) for i in xrange(1,int(n**0.5)+1) if n%i==0 and i!=1)
	temp=str(n)
	new_list=[]
	for i in b:
		new_list.append(''.join((str(j) for j in i)))
	for i in xrange(len(new_list)):
		new_list[i]+=temp
	for i in new_list:
		if check(i):
			print n,i

for i in xrange(1,999999):
	factors(i)


