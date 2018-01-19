from chapter1 import *

# test sorting problem
list_a = [3, 4, 1, 0, -4, 9, 11, 3, 2]
sorted_a = insert_sort(list_a)
for i in sorted_a:
	print(i, end = '\t')
print('\n', end = '')
print('*' * 20)
# test search problem
list_b = [1, 2, 3, 4, 5, 5, 6, 9, 10, 11, 3, 2, 3]
index = mysearch(list_b, 3)
index = insert_sort(index)
for i in index:
	print(i, end = '\t')
print('\n', end = '')
print('*' * 20)
# test binary add up
biA = [1, 1, 0, 1, 0, 0, 1]
biB = [1, 1, 0, 1, 1, 1, 1]
biC = binary_add(biA, biB)
for i in biC:
	print(i, end=" ")
print('\n', end = '')
print('*' * 20)
# test selection sort
sorted_b = select_sort(list_a)
for i in sorted_b:
	print(i, end = '\t')
