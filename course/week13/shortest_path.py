from shortest_algos import Bellman_ford, Dijkstra
import numpy as np
from node_class import *
n_vertex = 1000
Gi = {} # incoming dic
Go = {} # outgoing dic
for i in range(1,n_vertex + 1):
	Gi[i] = []
	Go[i] = []
with open('g3.txt') as f:
	lines = f.readlines()
for line in lines:
	l = line.rstrip()
	l = l.split(sep=' ')
	tail = int(l[0])
	head = int(l[1])
	cost = int(l[2])
	Gi[head].append(node(tail, cost))
	Go[tail].append(node(head, cost))

# insert source 0 with cost to all other nodes 0
for k in Gi.keys():
	Gi[k].append(node(0,0))

Gi[0] = []
output = Bellman_ford(Gi,0)
print(output)

if output != 0:
	# assign new edge costs
	for v in Go.keys():
		for e in range(0, len(Go[v])):
			node_out = Go[v][e]
			node_out.key = node_out.key + output[v] - output[node_out.name]
			# Go[v][e] = node_out
	# compute shortest path using dijkstra
	dist_all = [] # to store the dist of all vertice pairs
	for s in range(1, n_vertex+1):
		dist_prim = Dijkstra(Go, s)
		# for d in dist_prim:
		# 	dist_prim[d] = dist_prim[d] -
		for m in dist_prim.keys():
			dist_prim[m] = dist_prim[m] - output[s] + output[m]
			if dist_prim[m] != 0: # not to itself
				dist_all.append(dist_prim[m])
		print(s/(n_vertex))
	print(sorted(dist_all)[0:10])
