import numpy as np
import pandas as pd
global state_list
global sort_list
def Topo_sort(G): # G is the data.frame with tail and head columns
	n_nodes = np.int64(np.max(G.max()))
	global state_list
	state_list = np.ones(n_nodes+1) # node number directly used as index, 0 is nothing 
	# stores whether or not the node is checked, 1 = not checked, 0 = checked
	global sort_list
	sort_list = np.zeros(n_nodes+1)
	global current_label
	current_label = n_nodes
	for i in range(1,n_nodes+1):
		if(state_list[i]):
			DFS(G,i)
	return sort_list

def DFS(G,i):
	global state_list
	state_list[i] = 0
	i_node = G[G['tail'] == i]
	for j in i_node.loc[:,'head']:
		if(state_list[j]):
			DFS(G,j)
	global sort_list
	global current_label
	sort_list[i] = current_label
	current_label -= 1

global sort_list
G = pd.read_excel('test.xlsx')
sort = Topo_sort(G)
print(sort)