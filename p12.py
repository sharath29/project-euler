def tri_number(i):
	while True:
		val=i*(i+1)/2
		j=2
		print val
		for k in xrange(2,int(val**0.5)+1):
			if val%k==0:
				j+=2
				if j>500:
					return val
		i+=1
print tri_number(1000)