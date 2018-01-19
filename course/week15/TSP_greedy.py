import numpy as np
import pandas as pd
def dist(a, b):
	distance = np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
	return distance

with open('nn.txt') as f:
	lines = f.readlines()
coords = np.empty((len(lines), 3))
i = 0
for l in lines:
	l = l.strip()
	l = l.split(sep=" ")
	coords[i,2] = int(l[0])
	coords[i,0] = float(l[1])
	coords[i,1] = float(l[2])
	i += 1
coords = pd.DataFrame(coords[:,0:2], index = coords[:,2])
n = len(coords)
path = 0
city_one = coords.loc[1,]
current_city = coords.loc[1,] # start from city 1
coords = coords.drop([1])
while not coords.empty:
	print(1-len(coords)/n)
	tmp = coords.apply(lambda x: dist(current_city, x), axis=1)
	next_city = tmp.argmin() # index of next visit
	distance = tmp.get_value(next_city)
	path += distance
	current_city = coords.loc[next_city,]
	coords = coords.drop([next_city])

path = path + dist(city_one, current_city)
print(path)