f = open('p022_names.txt', 'rU')

names,result = [],[]
names = f.readline().replace('\"','').split(',')
names.sort()
res=0
val={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
for index,i in enumerate(names):
	sum1=0
	for j in xrange(len(i)):
		sum1+=val[i[j]]
	res+=(index+1)*sum1
print res