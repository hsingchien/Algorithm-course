def kwiksort2(A, p, r):
	while p < r:
		q = partition(A, p, r)
		if q - p <= r - q:
			kwiksort2(A, p, q-1)
			p = q + 1
		else:
			kwiksort2(A, q+1, r)
			r = r-1
	

def partition(A, p, r):
	x = A[r]
	i = p - 1
	for j in range(p, r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i+1


A = [13,19,9,5,12,8,7,4,11,2,6,21]
kwiksort2(A, 0, len(A)-1)
print(A)