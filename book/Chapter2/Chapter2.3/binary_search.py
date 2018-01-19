from insert_sort_recur import *
import math
def binary_search(A, key, index = [0]):
	if len(A) > 1:
		q = math.floor(len(A)/2)
		L = A[0:q]
		R = A[q:]
		if R[0] > key:
			index = binary_search(L, key, index)
		else:
			index[0] = index[0] + q
			index = binary_search(R, key, index)
	return index

A = [3,2,5,5,5,1]
insert_sort_recur(A, len(A))
i = binary_search(A, 5)
print(i[0]+1)