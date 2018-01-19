import random
random.seed(10)
def random_select(A,p,r,i):
	if p == r:
		return A[p]
	else:
		q = random_partition(A,p,r)
		k = q-p+1
		if k == i:
			return A[q]
		elif k < i:
			return random_select(A,q+1,r,i-k)
		elif k > i:
			return random_select(A,p,q-1,i)
def random_partition(A,p,r):
	s = random.randint(p,r)
	A[r],A[s] = A[s], A[r]
	key = A[r]
	print('key', key)
	i = p-1
	for j in range(p,r): # end at r because key doesn't need to compare with itself
		if A[j] <= key: # <= is important, equal values will be moved too so that none will be lagged behind
			i += 1 # i tracks elements smaller than key
			A[j],A[i] = A[i],A[j]
		print('i', i, 'A',A)
	A[i+1],A[r] = A[r], A[i+1]
	return i+1 # return pivot index, since it will 

def random_select_iter(A, i):
	p = 0
	r = len(A)-1
	B = A.copy()
	k = -6 # any random negative number
	while k != i-1:
		k = random_partition(B,p,r)
		print('k', k, 'i', i)
		print(B)
		if k > i-1:
			print('before',B)
			B = B[0:k]
			print('truncate',B)
			r = k-1

		elif k < i-1:
			B = B[k+1:r+1]
			r = r - k - 1
			i = i - k - 1
			print(B)
	return B[k]
	



A=[1,3,2,2,5,3,1,0,9,4,7]
print(random_select_iter(A,5))
# print(random_select(A,0,len(A)-1,9))
print(sorted(A))





