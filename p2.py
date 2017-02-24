first=1
second=2
a=[first,second]
res=0
term=0
while res<=4000000:
	term=second+first
	if term%2==0:
		res+=term
	first=second
	second=term
print res+2