import tqdm
def two_sum(A, t): #A a dict
	for k in A.keys():
		ki = int(k)
		ni = t-ki
		n = str(ni)
		if(n in A.keys() and ni != ki):
			return True
	return False



d = {}
with open("2sum.txt") as f:
	lines = f.readlines()
for l in lines:
	l = l.rstrip()
	if(l in d):
		d[l] += 1
	else:
		d[l] = 1

count = 0
for t in tqdm.trange(10000,10001):
	# print((t+10000)/20000)
	if two_sum(d,t):
		count += 1
	print(t,',',count)
print('\n',count)