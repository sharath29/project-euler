a=0

def digit_square(x):
	res=0
	temp=str(x)
	for i in temp:
		res+=int(i)**2
	return res

def num_chain(n):
	count1,count89=0,0
	global a
	while 1:
		print n,
		ans=digit_square(n)

		if ans==1:
			count1+=1
		if ans==89:
			count89+=1
		if count1==2:
			print '\n'
			return
		if count89==2:
			a+=1
			print '\n'
			return
		n=ans


for i in xrange(1,10000000):
	num_chain(i)

print a