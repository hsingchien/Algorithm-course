import numpy as np
def opti_search(A, P): # A is the search key, P is the weight
	l = len(A)
	S = np.zeros([l,l])
	for k in range(0, l):
		for i in range(0, l-k):
			sum_P = np.sum(P[i:(i+k+1)])
			mi = np.inf
			for r in range(i,i+k+1):
				if i > r-1:
					s1 = 0
				else:
					s1 = S[i,r-1]
				if r+1 > i+k:
					s2 = 0
				else:
					s2 = S[r+1,i+k]
				if s1+s2 <= mi:
					mi = s1+s2
			S[i, i+k] = sum_P+mi
	return S[0,l-1]
A = [1,2,3,4,5,6,7]
P = [0.2,0.05,0.17,0.1,0.2,0.03,0.25]
res = opti_search(A,P)
print(res)

