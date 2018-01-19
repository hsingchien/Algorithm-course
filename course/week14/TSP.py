import itertools
import numpy as np
def dist(a,b):
	distance = np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	return distance

with open('tsp.txt') as f:
	lines = f.readlines()
city = {}
comb_index = {} # store the row number of each combination
i = 0
for s in lines:
	s = s.strip()
	s = s.split(sep = " ")
	x = float(s[0])
	y = float(s[1])
	city[i] = [x,y]
	i += 1
n = len(city)
A = np.ones([2**(n-1), n])*np.inf # 25 cities in total
A[0,0] = 0 # base case for 0, inf for others
# for i in range(0,):
# 	comb_index[str(i)] = i # set the base cases
i = 0
comb_index['0'] = 0
city_name = list(range(1,n))
for m in range(1,n):
	for s in itertools.combinations(city_name, m): # s is the subset with origin 0 neglected
		i += 1 # record current subset index
		s = list(s)
		s.insert(0,0)
		comb_index[",".join(map(str,s))] = i
		print(i/2**(n-1))
		for j in s[1:]: # j is non-zero destination, 0 index is always 0
			min_dist = np.inf
			no_j = list(filter(lambda x: x != j, s))
			no_j_key = ",".join(map(str,no_j))
			for k in no_j:
				path_dist = A[comb_index[no_j_key], k] + dist(city[k],city[j])
				if path_dist < min_dist:
					min_dist = path_dist
			A[i, j] = min_dist
result = []
for k in range(0, n):
	result.append(A[i,k]+dist(city[k], city[0]))
print(sorted(result))