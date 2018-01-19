data = {}
visit = {} # true = not yet visited, false = visited from other nodes
# del = visited as center node

# the strategy is to test all the permutations for each with less than distance of 2
def test_permus(s, dic, visit):
	# distance = 1
	reach_out = [] # a list branch out nodes
	for i in range(0,len(s)):
		s_p = s
		if(s[i] == '0'):
			s_p = s[0:i]+'1'+s[i+1:]
		else:
			s_p = s[0:i]+'0'+s[i+1:]
		if(s_p in dic.keys() and s_p in visit.keys() and visit[s_p]):
		 # not yet visited from other nodes
			dic[s_p] = dic[s]
			visit[s_p] = False
			reach_out.append(s_p)
	for i in range(0, len(s)): 
		for j in range(i+1,len(s)):
			s_p = s
			if(s[i] == '0'):
				s_p = s[0:i]+'1' + s[i+1:j]
			else:
				s_p = s[0:i]+'0' + s[i+1:j]
			if(s[j] == '0'):
				s_p = s_p + '1' + s[j+1:]
			else:
				s_p = s_p + '0' + s[j+1:]
			if(s_p in dic.keys() and s_p in visit.keys() and visit[s_p]):
				# if(visit[s_p]):
					 # not yet visited from other nodes
				dic[s_p] = dic[s]
				visit[s_p] = False
				reach_out.append(s_p)
	return reach_out


with open('cluster2.txt') as f:
	lines = f.readlines()
for i in lines:
	# print(i)
	i=i.replace(" ","")
	i = i.strip()
	data[i] = i
	visit[i] = True
stack = [i]
num = len(visit)
n_groups = 1
while(len(visit) > 0):
	print((num-len(visit))/num)
	while stack:
		k = stack[0]
		visit[k] = False
		output = test_permus(k, data, visit)
		stack.extend(output)
		stack.pop(0)
		print(len(stack))
		del visit[k]
	# n_groups += 1
	if(len(stack) == 0 and len(visit) != 0):
		stack =[list(visit)[0]]
		n_groups += 1

print(n_groups)


