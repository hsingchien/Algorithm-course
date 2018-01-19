import heapsort
import math
def heap_max(A):
	return A[0]

def extract_heap_max(A):
	heap_size = len(A)
	A[0], A[-1] = A[-1], A[0]
	heapsort.max_heapify(A, 0, heap_size-1)
	return A.pop()

def heap_increase_key(A,i,key):
	if A[i] >= key:
		print("key cannot be smaller than current value")
		return
	A[i] = key
	while i >1 and A[i] > A[math.ceil(i/2-1)]:
		A[i], A[math.ceil(i/2-1)] = A[math.ceil(i/2-1)], A[i]
		i = math.ceil(i/2-1)

def heap_insert_key(A, key):
	A.append(-math.inf)
	heap_increase_key(A, len(A)-1, key)


