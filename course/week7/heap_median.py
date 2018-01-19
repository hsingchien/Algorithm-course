import max_heap
import min_heap

def heap_median(h1, h2, key):
 # max heap h1 stores smaller half, min h2 stores bigger half and h2 >= h1
	if(not h1):
		h1.append(key) # first key add to h1
		return key
	elif(not h2): # adding the second key
		h1_max = max_heap.heap_max(h1)
		if(h1_max <= key):
			h2.append(key)
		else:
			h2.append(max_heap.extract_heap_max(h1))
			h1.append(key)
	else: # both are not empty
		h1_max = max_heap.heap_max(h1)
		h2_min = min_heap.heap_min(h2)
		s1 = len(h1)
		s2 = len(h2)
		if(s1==s2):
			if(key <= h2_min):
				max_heap.heap_insert_key(h1, key)
			else:
				max_heap.heap_insert_key(h1, min_heap.extract_heap_min(h2))
				min_heap.heap_insert_key(h2, key)
		else:
			if(key >= h1_max):
				min_heap.heap_insert_key(h2, key)
			else:
				min_heap.heap_insert_key(h2, max_heap.extract_heap_max(h1))
				max_heap.heap_insert_key(h1, key)
	return max_heap.heap_max(h1)


h1 = []
h2 = []
median = []
with open('Median.txt') as f:
	lines = f.readlines()
for i in lines:
	i = int(i)
	median.append(heap_median(h1,h2,i))
print(sum(median))

