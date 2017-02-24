for i in xrange(1,10000):
	a=reduce(lambda x,y:(x[1],x[0]+x[1]),xrange(i),[0,1])[0]
 	if len(str(a))==1000:
 		print i,a
 		exit()
