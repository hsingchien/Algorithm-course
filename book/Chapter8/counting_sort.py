import numpy as np
def count_sort(A,k):
	C = np.zeros(k+1,dtype = np.int)
	for i in A:
		C[i] += 1
	for i in range(1,k+1):
		C[i] += C[i-1]
	B = np.empty_like(A)
	# Index = np.empty_like(A)
	for i in range(np.shape(A)[0]-1, -1, -1): # reverse loop from end index to begin
		B[C[A[i]]-1] = A[i] # C stores the COUNT, minus 1 to make it index
		Index[C[A[i]]-1] = i
		C[A[i]] -= 1
	return Index
def count_sort_in_place(A,k):
	C = np.zeros(k+1,dtype = np.int)
	for i in A:
		C[i] += 1
	for i in range(1,k+1):
		C[i] += C[i-1]
	swapped_index = np.empty([1,0], dtype=int)
	for i in range(np.shape(A)[0]-1, -1, -1):
		if i in swapped_index:
			continue
		else:
			while(i != C[A[i]] - 1 ) :
				element_go = A[i] # this element will go to the right spot
				A[C[A[i]]-1], A[i] = A[i],A[C[A[i]]-1]
				swapped_index = np.append(swapped_index,C[element_go]-1)
				C[element_go] -= 1

A = np.array([3,3,5,2,1,5,4,6,1,3,11,8])
count_sort_in_place(A,np.max(A))
print(A)
