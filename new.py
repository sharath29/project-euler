
a,b=[],[]
with open('p096_sudoku.txt') as f:
	for i in f:
		a.append(i)
for i,j in enumerate(a):
	if (i)%10==0:
		pass
	else:	
		b.append(j[:-1])

temp1=[]
w=[]
for i,j in enumerate(b):
	if i%9==0:
		w.append(temp1)
		temp1=[]
	temp1.append(j)



#print n
#for i in n:
#	print i
#print '---------'



num=list('123456789')

def check_row(n,i,j):
	temp = list(set(list(n[i]))-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def check_column(n,i,j):
	temp = []
	for k in xrange(9):
		temp.append(n[k][j])
	temp = list(set(temp)-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def check_box(n,i,j):
	k=i/3
	m=j/3
	temp = []
	for l in xrange(k*3,(k+1)*3):
		for p in xrange(m*3,(m+1)*3):
			temp.append(n[l][p])
	temp = list(set(temp)-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def z(n,l,p):
	return list(set(check_column(n,l,p)).intersection(check_row(n,l,p)).intersection(check_box(n,l,p)))

def check(n,i,j):

	k=i/3
	m=j/3
	x=z(n,i,j)
	for l in xrange(k*3,(k+1)*3):
		for p in xrange(m*3,(m+1)*3):
			if n[l][p]=='0':
				if i!=l or j!=p:
					#print x
					x=list(set(x)-set(z(n,l,p)))
	#print x
	if len(x)==1:
		n[i] = n[i][:j]+x[0]+n[i][j+1:]

#for i in xrange(9):
#	for j in xrange(9):
#		if n[i][j]=='0':
#			check(n,i,j)


#check(n,4,1)
#for i in n:
#	print i

print '---------'

n=[]
for q in xrange(20):
	for i in xrange(9):
		for j in xrange(9):
			if n[i][j]=='0':
				k=z(n,i,j)
				if len(k)==1:
					n[i] = n[i][:j]+k[0]+n[i][j+1:]
	
	for i in xrange(9):
		for j in xrange(9):
			if n[i][j]=='0':
				check(n,i,j)



for i in n:
	print i







