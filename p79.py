with open('p079_keylog.txt') as f:
	file = f.readlines()

a=[]
for i in file:
	a.append(i[:-1])
x=[]
for i in a:
	x=list(set(x).union(list(i)))
print x

for j in x:
	print j
	left={''}
	right={''}
	for i in a:
		if set(j).intersection(list(i))==set(j):
			if i[0]==j:
				right |= {i[1]}
				right |= {i[2]}
			if i[1]==j:
				left |= {i[0]}
				right |= {i[2]}
			if i[2]==j:
				left |= {i[0]}
				left |= {i[1]}
	left.remove('')
	right.remove('')
	print left,right
	