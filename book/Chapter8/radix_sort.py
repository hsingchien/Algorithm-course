import numpy as np
def count_sort(A,k,j):
	C = np.zeros(k+1,dtype = np.int)
	for i in A:
		C[i[j]] += 1
	for i in range(1,k+1):
		C[i] += C[i-1]
	B = np.empty_like(A)
	for i in range(np.shape(A)[0]-1, -1, -1): # reverse loop from end index to begin
		B[C[A[i][j]]-1] = A[i] # C stores the COUNT, minus 1 to make it index
		C[A[i][j]] -= 1
	return B

def radix_sort(A, nd):
	l = np.empty([np.shape(A)[0],nd])
	for i in range(0,np.shape(A)[0]):
		temp = [int(d) for d in str(A[i]).zfill(nd)]
		l[i] = temp
	l = np.int_(l)	
	for j in range(nd-1,-1,-1):
		k = int(np.max(l,axis=0)[j])
		l = count_sort(l,k,j)
	return l

A=np.array([123,712,100,89,2,177])
B = radix_sort(A,3)
print(B)