import numpy as np
def dist(a, b):
	distance = np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
	return distance

with open('nn.txt') as f:
	lines = f.readlines()
coord_x = []
coord_y = []
for l in lines:
	l = l.strip()
	l = l.split(sep=" ")
	coord_x.append(float(l[1]))
	coord_y.append(float(l[2]))
x = coord_x.pop(0)
y = coord_y.pop(0)
city_one = [x,y]
path = 0
while coord_x:
	print(1-len(coord_y)/33708)
	n = len(coord_x)
	tmp = []
	for i in range(0,n):
		tmp.append(dist([x,y], [coord_x[i], coord_y[i]]))
	next_city = np.argmin(tmp)
	x = coord_x.pop(next_city)
	y = coord_y.pop(next_city)
	path += tmp[next_city]
path = path + dist(city_one, [x,y])
print(path)
