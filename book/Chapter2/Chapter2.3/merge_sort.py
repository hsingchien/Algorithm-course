import math
def merge_sort(A, p, r):
	if p < r - 1:
		q = math.floor((p + r) / 2)
		merge_sort(A, p, q)
		merge_sort(A, q, r)
		merge_sublist(A, p, q, r)


def merge_sublist(A, p, q, r):
	# print(p, q, r)
	L = A[p:q]
	R = A[q:r]
	print(A)
	L.append(math.inf)
	R.append(math.inf)
	k = p
	while L[0] != math.inf or R[0] != math.inf:
		if L[0] <= R[0]:
			A[k] = L[0]
			L.pop(0)
		else:
			A[k] = R[0]
			R.pop(0)
		k += 1
	# print("A:", end = '\t')
# 	for i in A[p:r]:
# 		print(i, end = ', ')
# 	print('\n')


# A = [10,4,2,4,9,11,-10,12,15,-2,-2,0,1,4,9]
# merge_sort(A, 0, len(A))
# for i in A:
# 	print(i, end = ", ")
A=[5,3,8,9,1,7,0,2,6,4]
merge_sort(A,0,len(A))
print(A)