from math import floor, ceil, inf
def max_heapify(A,i, heap_size = None):
	if heap_size == None:
		heap_size = len(A)
	left = 2*i+1
	right = 2*i+2
	if left < heap_size and A[left] > A[i] :
		largest = left
	else:
		largest = i
	if right < heap_size and A[right] > A[largest]:
		largest = right
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest, heap_size)

def build_max_heapify(A):
	heap_size = len(A)
	for i in range(floor(heap_size/2-1),-1,-1):
		max_heapify(A, i)

def heap_sort(A):
	heap_size = len(A)
	build_max_heapify(A)
	# print(A)
	for i in range(len(A)-1, 0, -1):
		A[0], A[i] = A[i], A[0]
		heap_size = heap_size-1
		max_heapify(A,0, heap_size)


def heap_max(A):
	return A[0]

def extract_heap_max(A):
	heap_size = len(A)
	A[0], A[-1] = A[-1], A[0]
	max_heapify(A, 0, heap_size-1)
	return A.pop()

def heap_increase_key(A,i,key):
	if A[i] >= key:
		print("key cannot be smaller than current value")
		return
	A[i] = key
	while i >0 and A[i] > A[ceil(i/2-1)]:
		A[i], A[ceil(i/2-1)] = A[ceil(i/2-1)], A[i]
		i = ceil(i/2-1)

def heap_insert_key(A, key):
	A.append(-inf)
	heap_increase_key(A, len(A)-1, key)

