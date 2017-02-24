b= reduce(lambda x,y:x*y,[int(i) for i in xrange(10,1,-1)])
a= reduce(lambda x,y:x*y,[int(i) for i in xrange(20,1,-1)])
print a/(b)