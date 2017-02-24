from bs4 import BeautifulSoup
from selenium import webdriver
import unicodedata
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www.sudoku.com/')

html = driver.page_source
soup = BeautifulSoup(html,'lxml')

values=[]
for tag in soup.find_all("td", class_="cell"):
   	values.append(tag.text)

values = [unicodedata.normalize('NFKD', i).encode('ascii','ignore') for i in values]
print values

build=[]
temp=[]
for i in values:
	if i == ' ':
		build.append('0')
	else:
		build.append(i)
	if len(build)%9==0:
		temp.append(''.join(build))
		build=[]

num=list('123456789')

def check_row(n,i,j):
	temp = list(set(list(n[i]))-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def check_column(n,i,j):
	temp = []
	for k in xrange(9):
		temp.append(n[k][j])
	temp = list(set(temp)-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def check_box(n,i,j):
	k=i/3
	m=j/3
	temp = []
	for l in xrange(k*3,(k+1)*3):
		for p in xrange(m*3,(m+1)*3):
			temp.append(n[l][p])
	temp = list(set(temp)-set(['0']))
	if set(num)==set(temp):
		return True
	else:
		return list(set(num)-set(temp))

def z(n,l,p):
	return list(set(check_column(n,l,p)).intersection(check_row(n,l,p)).intersection(check_box(n,l,p)))

def check_next_grid(n,i,j):
	j+=1
	if j>9:
		j=0
		i+=1
	if len(z(n,i,j))==0:
		return False
	else:
		return True

def find_empty_location(n,l):
	for i in xrange(9):
		for j in xrange(9):
			if n[i][j]=='0':
				l[0]=i
				l[1]=j
				return True
	return False

def check_location_safe(n,i,j,num):
	if num in z(n,i,j):
		return True
	return False

def solve(n):
	l = [0,0]
	if not find_empty_location(n,l):
		return True
	i=l[0]
	j=l[1]

	for k in xrange(1,10):
		num=str(k)
		if(check_location_safe(n,i,j,num)):
			n[i] = n[i][:j]+num+n[i][j+1:]
			if(solve(n)):
				return True
			n[i] = n[i][:j]+'0'+n[i][j+1:]

	return False

solve(temp)
for i in temp:
	print i

