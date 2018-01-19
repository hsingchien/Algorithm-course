import min_heap as mh
from symbol import symbol


weights = []
wdic = {}
k = 0
with open('huffman.txt') as f:
	lines = f.readlines()
for i in lines:
	i = int(i)
	weights.append(symbol(i, [k]))
	wdic[k] = 0
	k += 1
# build the heap
mh.build_min_heapify(weights)
while len(weights)>1:
	s1 = mh.extract_heap_min(weights)
	s2 = mh.extract_heap_min(weights)
	s3 = s1 + s2
	l3 = s3.list
	for i in l3:
		wdic[i] = wdic[i] + 1
	mh.heap_insert_key(weights,s3)
length = []
for k in wdic.keys():
	length.append(wdic[k])
mh.heap_sort(length)
print(len(length))
print(length)


# s1 = mh.extract_heap_min(weights)
# s2 = mh.extract_heap_min(weights)
# s3 = s1+s2
# mh.heap_insert_key(weights,s3)