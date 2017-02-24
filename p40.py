res=''
for i in xrange(1000000):
	res+=str(i)
print int(res[1])*int(res[10])*int(res[100])*int(res[1000])*int(res[10000])*int(res[100000])*int(res[1000000])