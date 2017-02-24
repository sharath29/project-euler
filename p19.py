import calendar as cal
count = 0
for i in xrange(1901,2001):
	for j in xrange(1,13):
		if cal.weekday(i,j,1) == 6:
			count+=1
print count
