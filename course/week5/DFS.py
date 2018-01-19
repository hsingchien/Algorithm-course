import numpy as np
import pandas as pd
def DFS_loop(G, ft=np.array([])):
	global t
	t = 0
	global s
	s = None
	n_nodes = n_nodes = np.max(G.max())
	global state_list
	state_list = np.ones(n_nodes+1)
	state_list[0] = 0
	global leader
	leader = np.zeros(n_nodes+1)
	global f_time
	f_time = np.zeros(n_nodes+1)
	if(not ft.any()):
		for i in range(1,n_nodes+1):
			# print(i/n_nodes,end="*")
			if(state_list[i]):
				# s = i
				DFS(G,i)
	else:
		# print(ft[np.argsort(ft*-1)])
		# print(np.argsort(ft*-1)[0:len(ft)-1])
		for i in np.argsort(ft*-1)[0:len(ft)]:
			if(state_list[i]):
				s = i
				DFS(G,i)
	return [f_time, leader]



def DFS(G, i): # depth first search
	global state_list
	# state_list[i] = 0
	global leader
	# leader[i] = s
	rec_stack = [i]
	global f_time
	global t
	while(rec_stack):
		cur_node = rec_stack[len(rec_stack)-1] # top node on stack
		# print(cur_node,end='\t')
		# print(rec_stack)
		# print(state_list)
		if(state_list[cur_node] or f_time[cur_node] == 0):
			state_list[cur_node] = 0
			cur_node_child = G[G['tail'] == cur_node].loc[:,'head']
			# print('child',cur_node_child)
			if(np.any(state_list[cur_node_child])):
				# print('non',np.nonzero(state_list[cur_node_child]))
				cur_node_child = cur_node_child.iloc[np.nonzero(state_list[cur_node_child])]
				rec_stack.extend(cur_node_child)
			else:
				cur_node = rec_stack.pop()
				t += 1
				f_time[cur_node] = t
				leader[cur_node] = s 
				# state_list[cur_node] = 0
		else:
			rec_stack.pop()

global f_time
G = pd.read_excel('test.xlsx')
sort = DFS_loop(G)
# print(f_time)
ft = np.copy(f_time)
G_r = G.copy()
G_r.columns = ['head', 'tail']
sort2 = DFS_loop(G_r,ft)
scc_count = np.bincount(np.int64(sort2[1]))
scc_count = scc_count[np.nonzero(scc_count)]
print(scc_count)







