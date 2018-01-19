from node_class import node, node_list
import heap_pack as hp
import numpy as np

G = {}
with open("edges.txt") as dj:
	lines = dj.readlines()
for i in lines:
	l = i.split(sep=' ')
	name1 = int(l[0]) # name of one end
	name2 = int(l[1]) # name of the other end
	cost = int(l[2]) # cost of the edge
	if(name1 in G):
		G[name1].append(node(name2, cost))
	else:
		G[name1] = [node(name2, cost)]
	if(name2 in G):
		G[name2].append(node(name1, cost))
	else:
		G[name2] = [node(name1, cost)]





#initialize pointer
n_list = []
for i in range(0,501):
	n_list.append(node(i,np.inf))
n_list[1].key = 0 # initialize heap, node 1 is already visited
n_list = node_list(n_list) 
hp.build_min_heapify(n_list)
A = 0 # A is the sum of MST
B = {1:[1]} # B store visited nodes
while G:
	cur_visit = hp.extract_heap_min(n_list) # a node object with name and key
	A += cur_visit.key
	cur_visit_outgo = G[cur_visit.name] # a list of branching outs of next node
	B[cur_visit.name] = [1]
	del G[cur_visit.name] # delete visited node from G
	for i in cur_visit_outgo:
		if i.name in G:
			ind = n_list.pointer[i.name] # get the index of target node in the heap
			# if cur node leads to a smaller route value, then update the route to 
			# cur node
			route_select = hp.heap_decrease_key(n_list, ind, i.key)


print(A)
