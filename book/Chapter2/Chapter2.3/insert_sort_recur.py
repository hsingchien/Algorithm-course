def insert_sort_recur(A, l):
	if l > 0:
		insert_sort_recur(A, l - 1)
	key = A[l-1]
	i = l - 2
	while i >= 0 and A[i] >= key:
			A[i+1] = A[i]
			i = i - 1
	A[i+1] = key


# A = [3, -1, 2, -1, -5, 7, 9, -11, 0, 6, 4]
# insert_sort_recur(A, len(A))
# for i in A:
# 	print(i)


