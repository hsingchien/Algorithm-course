import math
def merge_sort_inv_pair(A, p, r, n):
	if p < r - 1:
		q = math.floor((p + r) / 2)
		n = merge_sort_inv_pair(A, p, q, n)
		n = merge_sort_inv_pair(A, q, r, n)
		n = merge_sublist(A, p, q, r, n)
	return n


def merge_sublist(A, p, q, r, n):
	# print(p, q, r)
	L = A[p:q]
	R = A[q:r]
	L.append(math.inf)
	R.append(math.inf)
	k = p
	while L[0] != math.inf or R[0] != math.inf:
		# print(L)
		# print(R)
		# print(n)
		# print("*" * 20)
		if L[0] <= R[0]:
			A[k] = L[0]
			L.pop(0)
		else:
			A[k] = R[0]
			if L[0] != math.inf:
				n += len(L) - 1
			print(n)
			R.pop(0)
		k += 1
	return n


A = list(range(6,0,-1))
n = 0
n = merge_sort_inv_pair(A, 0, len(A), n)
print(A)
print(n)
