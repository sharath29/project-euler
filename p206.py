# a = int(1929394959697989990**0.5)
# b = int(1020304050607080900**0.5)
# print a,b
# for i in xrange(a,b,-1):
# 	if str(i*i)[::2]=='1234567890':
# 		print i
# 		break
# 	else:
# 		continue
for i in xrange(138902663,101010101,-1):
 	if str(100*i*i)[0::2] == '1234567890':
 		print i*10
 		break