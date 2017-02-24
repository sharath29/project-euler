for i in xrange(1000,1,-1):
	for j in xrange(1000,1,-1):
		for k in xrange(1000,1,-1):
			#print i,j,k
			if (i**2 + j**2)==(k**2):
				if (i+j+k)==1000:
					print i*j*k