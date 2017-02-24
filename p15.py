a=reduce(lambda x,y:x*y,[int(i) for i in xrange(40,1,-1)])
b=reduce(lambda x,y:x*y,[int(i) for i in xrange(20,1,-1)])
print a/(b*b)