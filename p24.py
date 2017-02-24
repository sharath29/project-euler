import itertools
a=list(itertools.permutations(range(10)))[999999]
res=''
for i in a:
	res+=str(i)
print res
