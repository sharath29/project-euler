with open("triangle_file.txt","r") as f:
    content = f.read().splitlines()

matrix = [[0 for i in range(5)] for j in range(5)]
matrix[0][0]=5
triangle=[]

for i in content:
	triangle.append(i.split(' '))

for i in xrange(len(triangle)-2,0,-1):
	for j in xrange(len(triangle[i])):
		triangle[i][j]=int(triangle[i][j])+max(int(triangle[i+1][j]),int(triangle[i+1][j+1]))

print max(triangle[1][0],triangle[1][1])+int(triangle[0][0])