'''matrix=[[0 for i in xrange(1001)] for j in xrange(1001)]
a=[]
for i in xrange(1,1002):
	if i%2 != 0:
		a.append(i)	
'''
with open("13.txt") as it:
	n=it.read().splitlines()
sum1=25
print n
for i in n:
	sum1+=int(i)
print sum1


'''	
temp=9

for i in [2*i for i in xrange(2,1000000)]:
	for j in xrange(4):
		temp+=i
		print temp
	if temp >1001*1001:
		break
'''