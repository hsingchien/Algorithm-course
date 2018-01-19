from node_class import node, node_list
import heap_pack as hp
import numpy as np

G = {}
with open("dijkstra.txt") as dj:
	lines = dj.readlines()
for i in lines:
	l = i.split(sep='\t')
	name = int(l[0]) # name of node, use as keys for dictionary storing the graph
	l = l[1:]
	tmp = []
	for i in l: # each has format of 'node_name, value'
		s = i.split(sep=',')
		if(s != ['\n']):
			n_name = int(s[0])
			value = int(s[1])
			tmp.append(node(n_name,value)) # each node connection is saved as a sub-dict
	G[name] = tmp
# print_nodes_list(G['1'])


#initialize pointer
n_list = []
for i in range(0,201):
	n_list.append(node(i,np.inf))
n_list[1].key = 0 # initialize heap, node 1 is already visited
n_list = node_list(n_list) 
hp.build_min_heapify(n_list)
A = {} # A store value
B = {1:[1]} # B store route
while G:
	cur_visit = hp.extract_heap_min(n_list) # a node object with name and key
	A[cur_visit.name] = cur_visit.key
	cur_visit_outgo = G[cur_visit.name] # a list of branching outs of next node
	del G[cur_visit.name] # delete visited node from G
	for i in cur_visit_outgo:
		if i.name in G:
			ind = n_list.pointer[i.name] # get the index of target node in the heap
			# if cur node leads to a smaller route value, then update the route to 
			# cur node
			route_select = hp.heap_decrease_key(n_list, ind, cur_visit.key + i.key)
			if route_select:
				cur_route = B[cur_visit.name].copy()
				cur_route.append(i.name)
				B[i.name] = cur_route


print(A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197])
print(B[7],B[37],B[59],B[82],B[99],B[115],B[133],B[165],B[188],B[197])
