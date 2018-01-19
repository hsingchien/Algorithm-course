from math import floor, ceil, inf
def min_heapify(A,i, heap_size = None):
	if heap_size == None:
		heap_size = len(A)
	left = 2*i+1
	right = 2*i+2
	if left < heap_size and A[left] < A[i] :
		smallest = left
	else:
		smallest = i
	if right < heap_size and A[right] < A[smallest]:
		smallest = right
	if smallest != i:
		A[i], A[smallest] = A[smallest], A[i]
		min_heapify(A, smallest, heap_size)

def build_min_heapify(A):
	heap_size = len(A)
	for i in range(floor(heap_size/2-1),-1,-1):
		min_heapify(A, i)

def heap_sort(A):
	heap_size = len(A)
	build_min_heapify(A)
	# print(A)
	for i in range(len(A)-1, 0, -1):
		A[0], A[i] = A[i], A[0]
		heap_size = heap_size-1
		min_heapify(A,0, heap_size)


def heap_min(A):
	return A[0]

def extract_heap_min(A):
	heap_size = len(A)
	A[0], A[-1] = A[-1], A[0]
	min_heapify(A, 0, heap_size-1)
	return A.pop()

def heap_decrease_key(A,i,key):
	if A[i] <= key:
		print("key cannot be larger than current value")
		return
	A[i] = key
	while i > 0 and A[i] < A[ceil(i/2-1)]:
		A[i], A[ceil(i/2-1)] = A[ceil(i/2-1)], A[i]
		i = ceil(i/2-1)

def heap_insert_key(A, key):
	A.append(inf)
	heap_decrease_key(A, len(A)-1, key)


# A = [3,2,5,6,5,4,7,10]
# build_min_heapify(A)
# heap_insert_key(A,1)
# heap_decrease_key(A,5,0)
# heap_sort(A)
# print(A)