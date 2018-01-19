def H_kwiksort(A, p, r):
	if p < r:
		s = H_partition(A, p, r)
		H_kwiksort(A, p, s)
		H_kwiksort(A, s+1, r)

def H_partition(A, p, r):
	x = A[p]
	i = p - 1
	j = r + 1
	while True:
		i += 1
		j -= 1
		while A[j] > x:
			j -= 1
		while A[i] < x:
			i += 1
		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j


A = [13,19,9,5,12,8,7,4,11,2,6,21]
j = H_partition(A,0,len(A)-1)
print(A)
print(j)
H_kwiksort(A, 0, len(A)-1)
print(A)