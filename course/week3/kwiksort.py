import pandas as pd
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
	x = A[p]
	i = p
	for j in range(p+1, r+1):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i], A[p] = A[p], A[i]
	return i


A = pd.read_excel('data.xlsx')
A = A.iloc[:,0].values.tolist()

kwiksort(A, 0, len(A)-1)
print(n)
