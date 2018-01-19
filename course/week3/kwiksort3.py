import pandas as pd
import math
import statistics
import numpy as np
global n
n = 0

def kwiksort(A, p, r):
	global n
	if p < r:
		q = partition(A, p, r)
		n = n+(r-p)
		# print(q)
		kwiksort(A, p, q-1)
		kwiksort(A, q+1, r)
def partition(A, p, r):
	k = math.floor((p+r)/2)
	inds = [p,k,r]
	ind = np.argsort([A[p],A[k],A[r]])[3//2]
	ind = inds[ind]
	A[p],A[ind] = A[ind],A[p]
	x = A[p]
	i = p
	for j in range(p+1, r+1):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i], A[p] = A[p], A[i]
	return i


# print(np.argsort([4,2,6])[len([3,4,5])//2])
A = pd.read_excel('data.xlsx')
A = A.iloc[:,0].values.tolist()
# A = [2,5,1,3,4]
kwiksort(A, 0, len(A)-1)
print(n)
