'''a,b=[],[]
with open('p096_sudoku.txt') as f:
	for i in f:
		a.append(i)
for i,j in enumerate(a):
	if (i)%10==0:
		pass
	else:	
		b.append(j[:-2])
'''
n = [
'003020600',
'900305001',
'001806400',
'008102900',
'700000008',
'006708200',
'002609500',
'800203009',
'005010300']






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

#if (check_box(n,i,j) or check_row(n,i,j) or check_column(n,i,j)) == True:
	#return True //no need to change
for i in xrange(9):
	for j in xrange(9):
		if n[i][j]=='0':
			if len(list(set(check_column(n,i,j)).intersection(check_row(n,i,j)).intersection(check_box(n,i,j))))==1:
				n[i] = n[i][:j]+'h'+n[i][j+1:]








