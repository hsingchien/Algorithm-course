from math import floor

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


a = [5,3,2,9,1,3,4,6]
heap_sort(a)
print(a)
