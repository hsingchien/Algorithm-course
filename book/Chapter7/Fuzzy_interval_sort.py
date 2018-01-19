import random as rand
rand.seed(a = 17)
def find_intersection(A, p, s):
	r = rand.randrange(p, s+1)
	x = A[r].copy()
	A[s],A[r] = A[r],A[s]
	for i in range(p, s):
		if x[1] >= A[i][0] and x[0] <= A[i][1]:
			x[0] = max(x[0], A[i][0])
			x[1] = min(x[1], A[i][1])
	return x
def partition_right(A, p, s, x):
	a = x[0]
	i = p - 1
	for j in range(p, s+1):
		if A[j][0] <= a:
			i += 1
			A[i],A[j] = A[j],A[i]
	return i+1
def partition_left(A, p, s, x):
	b = x[1]
	print(b)
	i = p - 1
	for j in range(p, s+1):
		# print(A[j][1])
		if A[j][1] < b:
			i += 1
			A[i],A[j] = A[j],A[i]
			# print(A)
	return i+1
def fuzzy_sort(A, p, s):
	if p < s:
		pivot = find_intersection(A,p,s)
		print(pivot)
		r = partition_right(A,p,s, pivot)
		q = partition_left(A,p,r, pivot)
		fuzzy_sort(A, p, q-1)
		fuzzy_sort(A, r+1, s)



A = [[2,5],[6,7],[4,6],[1,3],[3,4],[10,12],[23,27],[18,24],[9,19]]
fuzzy_sort(A,0,len(A)-1)
print(A)