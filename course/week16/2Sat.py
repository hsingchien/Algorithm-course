from DFS import DFS_loop
import numpy as np

C = {}
C_r = {}
vertices = []
with open('2sat6.txt') as f:
	lines = f.readlines()
for l in lines:
	l = l.strip()
	l = l.split(sep=" ")
	lit1 = int(l[0])
	lit2 = int(l[1])
	if not -lit1 in C.keys():
		C[-lit1] = [lit2]
	else:
		C[-lit1].append(lit2)
	if not -lit2 in C.keys():
		C[-lit2] = [lit1]
	else:
		C[-lit2].append(lit1)
	if not lit1 in C.keys():
		C[lit1] = []
	if not lit2 in C.keys():
		C[lit2] = []
	if not lit2 in C_r.keys():
		C_r[lit2] = [-lit1]
	else:
		C_r[lit2].append(-lit1)
	if not lit1 in C_r.keys():
		C_r[lit1] = [-lit2]
	else:
		C_r[lit1].append(-lit2)
	if not -lit1 in C_r:
		C_r[-lit1] = []
	if not -lit2 in C_r:
		C_r[-lit2] = []
	vertices.append(lit1)
	vertices.append(lit2)
	vertices.append(-lit1)
	vertices.append(-lit2)
vertices = np.unique(vertices)
sort1 = DFS_loop(C, vertices)
sort2 = DFS_loop(C_r, vertices, sort1[0])
group = sort2[1]
solution = True

for k in group.keys():
	if group[-k] == group[k]:
		print('no solution')
		print(k, group[k])
		print(-k, group[-k])
		solution = False
		break
if solution:
	print('solvable')
