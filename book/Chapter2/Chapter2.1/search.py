def mysearch(input_list, key):
	output_index = []
	i = len(input_list) - 1
	while i >= 0:
		if input_list[i] == key:
			output_index.append(i)
		i -= 1
	return output_index

list_a = [1, 2, 3, 4, 5, 5, 6, 9, 10, 11, 3, 2, 3]
index = mysearch(list_a, 3)
index = insert_sort(index)
for i in index:
	print(i)
