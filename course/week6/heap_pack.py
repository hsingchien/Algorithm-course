import math


def min_heapify(A,i, heap_size = None): # A is node_list type
	if heap_size == None:
		heap_size = len(A.list)
	left = 2*i+1
	right = 2*i+2
	if left < heap_size and A.list[left] < A.list[i] :
		smallest = left
	else:
		smallest = i
	if right < heap_size and A.list[right] < A.list[smallest]:
		smallest = right
	if smallest != i:
		A.list[i], A.list[smallest] = A.list[smallest], A.list[i]
		A.pointer[A.list[i].name], A.pointer[A.list[smallest].name] = A.pointer[A.list[smallest].name], A.pointer[A.list[i].name]
		min_heapify(A, smallest, heap_size)

def build_min_heapify(A):
	heap_size = len(A.list)
	for i in range(math.floor(heap_size/2-1),-1,-1):
		min_heapify(A, i)

def heap_sort(A):
	heap_size = len(A.list)
	build_min_heapify(A.list)
	# print(A)
	for i in range(len(A.list)-1, 0, -1):
		A.list[0], A.list[i] = A.list[i], A[0]
		A.pointer[A.list[0].name], A.pointer[A.list[i].name] = A.pointer[A.list[i].name], A.pointer[A.list[0].name]
		heap_size = heap_size-1
		min_heapify(A,0, heap_size)

def heap_min(A):
	return A.list[0]

def extract_heap_min(A):
	heap_size = len(A.list)
	A.list[0], A.list[-1] = A.list[-1], A.list[0]
	A.pointer[A.list[0].name], A.pointer[A.list[-1].name] = A.pointer[A.list[-1].name], A.pointer[A.list[0].name]
	min_heapify(A, 0, heap_size-1)
	return A.list.pop()

def heap_decrease_key(A,i,key):
	# print(i, len(A.list))
	if A.list[i].key <= key:
		# print("key cannot be larger than current value")
		return False
	A.list[i].key = key
	while i >1 and A.list[i] < A.list[math.ceil(i/2-1)]:
		A.list[i], A.list[math.ceil(i/2-1)] = A.list[math.ceil(i/2-1)], A.list[i]
		A.pointer[A.list[i].name], A.pointer[A.list[math.ceil(i/2-1)].name] = A.pointer[A.list[math.ceil(i/2-1)].name], A.pointer[A.list[i].name]
		i = math.ceil(i/2-1)
	return True

# def heap_insert_key(A, key):
# 	A.append(math.inf)
# 	heap_decrease_key(A, len(A)-1, key)




