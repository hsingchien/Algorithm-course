import numpy as np
def DFS_loop(G, vertices, ft={}): # G is a dict with each value store the outgoing list
	global t
	t = 0
	global s
	s = None
	n_nodes = len(G)
	global state_list
	global v_f_time
	state_list = {}
	v_f_time = {}
	for i in vertices:
		state_list[i] = 1
		v_f_time[i] = 0
	global leader
	leader = {}
	global f_time
	f_time = {} # key is the finish time, value is the vertex
	if(not ft): # if finish time matrix is not given (i.e. for SCC first run)
		for i in G.keys():
			# print(i/n_nodes,end="*")
			if(state_list[i]): # if not visted
				# s = i
				DFS(G, i)
	else:
		# print(ft[np.argsort(ft*-1)])
		# print(np.argsort(ft*-1)[0:len(ft)-1])
		ft_keys = list(ft.keys())
		ft_keys.reverse()
		for i in ft_keys: # dfs by finish time is decreasing order
			if(state_list[ft[i]]):
				s = ft[i]
				DFS(G, ft[i])
	return [f_time, leader]



def DFS(G, i): # depth first search
	global state_list
	# state_list[i] = 0
	global leader
	# leader[i] = s
	rec_stack = [i]
	global f_time
	global v_f_time
	global t
	while(rec_stack):
		cur_node = rec_stack[len(rec_stack)-1] # top node on stack
		# print(cur_node,end='\t')
		# print(rec_stack)
		# print(state_list)
		if(state_list[cur_node] or v_f_time[cur_node] == 0):
			state_list[cur_node] = 0
			cur_node_child = G[cur_node] # a list of outgoing 
			# print('child',cur_node_child)
			unvisited_child = [x for x in cur_node_child if state_list[x] != 0]
			if unvisited_child:
				# print('non',np.nonzero(state_list[cur_node_child]))
				rec_stack.extend(unvisited_child)
			else:
				cur_node = rec_stack.pop()
				t += 1
				v_f_time[cur_node] = t
				f_time[t] = cur_node
				leader[cur_node] = s 
				# state_list[cur_node] = 0
		else:
			rec_stack.pop()

# global f_time
# G = {}
# G_r = {}
# vertices = []
# with open('test.txt') as f:
# 	lines = f.readlines()
# for l in lines:
# 	l = l.strip()
# 	l = l.split(sep=" ")
# 	tail = int(l[0])
# 	head = int(l[1])
# 	vertices.append(tail)
# 	vertices.append(head)
# 	if not tail in G.keys():
# 		G[tail] = [head]
# 	else:
# 		G[tail].append(head)
# 	if not head in G_r.keys():
# 		G_r[head] = [tail]
# 	else:
# 		G_r[head].append(tail)
# 	if not head in G.keys():
# 		G[head] = []
# 	if not tail in G_r.keys():
# 		G_r[tail] = []
# # print(G_r)
# vertices = np.unique(vertices)
# sort1 = DFS_loop(G, vertices)
# # print(sort1[0])
# sort2 = DFS_loop(G_r, vertices, sort1[0])
# out = np.array([sort2[1][x] for x in sort2[1].keys()])
# # print(sort2[1])
# out = out + np.absolute(np.min(out))
# out = np.bincount(out)
# print(np.sort(out[np.nonzero(out)]))






