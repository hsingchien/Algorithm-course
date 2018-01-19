V = []
with open('mwis.txt') as f:
	lines = f.readlines()
for i in lines:
	V.append(int(i))
# build the IS array
IS = V[0:2]
for i in V[2:]:
	res = max(IS[-1], IS[-2]+i)
	IS.append(res)
print(len(IS))
i = len(IS)-1
S = []
while(i>=1):
	if IS[i] == IS[i-1]:
		i -= 1
	else:
		S.append(i+1)
		i -= 2
print(S)
# i=999
# S2 = []
# while(i>=1):
# 	if IS[i-1] >= IS[i-2] + V[i]:
# 		# case 1 wins, no i
# 		i -= 1
# 	else:
# 		S2.append(i)
# 		i -= 2
# print(S2)
# reconstruct path