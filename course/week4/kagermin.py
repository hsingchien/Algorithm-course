import numpy as np
import pandas as pd
import copy
tmp = list()
with open('Mincut.txt') as f:
	lines = f.readlines()
for i in range(0, len(lines)):
	st = lines[i]
	st = np.fromstring(st, dtype = int, sep = '\t')
	tmp.append(st)
def kager(tmp):
	n_node = np.arange(0,len(tmp)) # index of effective nodes left
	while(np.shape(n_node)[0] > 2):
		#step 1 select node1 and node2
		node1 = np.random.choice(n_node)+1 # notes the node's name not index
		node1_connect = tmp[node1-1][1:]
		node2 = np.random.choice(node1_connect)
		node2_connect = tmp[node2 - 1][1:] # node2 - 1 is the node2 index
		#step 2 cat node1 node2 profile, eliminate self loops
		temp_connect = np.concatenate((node1_connect, node2_connect))
		temp_connect = temp_connect[~np.in1d(temp_connect,[node1,node2])]
		tmp[node1-1] = np.insert(temp_connect,0,node1)
		#step 3 change names of node2 in other arrays to node1
		# print(node1, node2)
		for i in n_node:
			s = tmp[i][1:]
			s[s == node2] = node1
		#step 4 delete node2 in effective node list
		n_node = n_node[n_node!=(node2-1)]
		# print(tmp)
	return n_node
exa = [np.array([1,2,2]),np.array([2,1,1,3]),np.array([3,2,4,4]),np.array([4,3,3])]
result = np.empty(500)
# n_node = kager(tmp)
# print(tmp[n_node[0]])
# print(tmp[n_node[1]])
for i in range(0,500):
	ttmp = copy.deepcopy(tmp)
	n_node = kager(ttmp)
	# print(n_node)
	con = ttmp[n_node[0]]
	# print('con',con,'kkk')
	result[i] = np.shape(con)[0]-1
# print(result)
print(np.min(result))

