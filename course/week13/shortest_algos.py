import copy
import numpy as np
import heap_pack as hp
from node_class import node, node_list
def Bellman_ford(G, s):
# input G has a form of dic, with eatch key correspond to a vertex and store the incoming
# node list G['1'] = [node(name1, cost1), node(name2, cost2), etc.]
# return a dictionary, keys are node names and values are the shortest path lengh
# or if a negative cycle exist, return 0.
# s is an int
	n = len(G)
	tb = np.ones([n,n+1]) * np.inf
	tb[s,0] = 0
	for i in range(1,n+1):
		for k in G.keys():
			node_l = G[k]
			min_value = np.inf
			for m in node_l:
				name = m.name
				cost = m.key
				if tb[name,i-1] + cost < min_value:
					min_value = tb[name,i-1] + cost
			if tb[k,i-1] < min_value:
				tb[k,i] = tb[k,i-1]
			else:
				tb[k,i] = min_value
	if np.all(tb[:,n] == tb[:,n-1]): # no negative circle
		return dict(enumerate(tb[:,n-1]))
	else:
		return 0


def Dijkstra(Go, s):
# take input G having the same form, output a dictionary with each key corresponds
# to a vertex and value is the shortest path length.
	G = copy.deepcopy(Go)
	n_list = []
	for i in range(0, len(G)+1):
		n_list.append(node(i,np.inf))
	n_list[s].key = 0 # initialize heap, node s is already visited
	n_list = node_list(n_list) 
	hp.build_min_heapify(n_list)
	A = {} # A store value
	while G:
		cur_visit = hp.extract_heap_min(n_list) # a node object with name and key
		A[cur_visit.name] = cur_visit.key
		if cur_visit.name in G:
			cur_visit_outgo = G[cur_visit.name] # a list of branching outs of next node
		
			del G[cur_visit.name] # delete visited node from G
			for i in cur_visit_outgo:
				if i.name in G: # rule out the ones visited
					ind = n_list.pointer[i.name] # get the index of target node in the heap
					# if cur node leads to a smaller route value, then update the route to 
					# cur node
					hp.heap_decrease_key(n_list, ind, cur_visit.key + i.key)
		else:
			for d in n_list.list:
				A[d.name] = d.key

	return A