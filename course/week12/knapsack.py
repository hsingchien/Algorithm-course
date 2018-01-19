import numpy as np

def Knap(W, V, Wt):
	n = len(W)
	dic = {} # store the optimal value of 'n,W' with the key 'n,W'
	t1 = [n-1, Wt] # initial coordinate
	stack = [t1]
	while stack:
		print(len(stack))
		last = stack[len(stack)-1]
		n_l = last[0]
		w_l = last[1]
		key = str(n_l) + ',' + str(w_l)
		child1_n = n_l - 1
		child1_w = w_l - W[n_l]
		child2_n = n_l - 1
		child2_w = w_l
		key1 = str(child1_n)+','+str(child1_w)
		key2 = str(child2_n)+','+str(child2_w)
		if(not (key1 in dic.keys() and key2 in dic.keys())): 
		# not able to calculate the last one
			if(not key1 in dic.keys()):
				if(child1_n < 0 or child1_w <= 0):
					dic[key1] = 0
				else:
					stack.append([child1_n,child1_w])

			if(not key2 in dic.keys()):
				if(child2_n >= 0):
					stack.append([child2_n, child2_w])
				else:
					dic[key2] = 0
		else:
			if child1_w >= 0: 
				dic[key] = max(dic[key1] + V[n_l], dic[key2])
			else:
				dic[key] = max(dic[key1], dic[key2])
			stack.pop()
	key_want = str(n-1) + ',' + str(Wt)
	# for i in dic.keys():
	# 	print(i,dic[i])
	return dic[key_want]

W = []
V = []
Wt = 10000
with open('knapsack1.txt') as f:
	lines = f.readlines()
	for l in lines:
		l = l.split(sep = ' ')
		V.append(int(l[0]))
		W.append(int(l[1]))
print(Knap(W,V,Wt))



