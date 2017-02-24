a = []

def sum_of_digits(n):
	return reduce(lambda x,y: x+y, [int(i) for i in str(n)])

for i in xrange(2,100):
	for j in xrange(2,100):
		a.append(sum_of_digits(j**i))

print max(a)