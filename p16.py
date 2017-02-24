a=reduce(lambda x,y:x*y,[int(i) for i in xrange(100,1,-1)])
print reduce(lambda x,y: x+y,[int(i) for i in str(a)])