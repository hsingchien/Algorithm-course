def find_subarray(item, evens):
	output_index = evens.copy()
	n_rows = len(item)
	n_cols = len(item[0])
	if(len(evens) < 0.5 * n_rows): # item is odd numbered matrix
		evens.append(n_cols-1)
	evens.insert(0, 0) 
	for i in range(0, n_rows, 2):
		odd_row = item[i]
		minimum = odd_row[0]
		index = 0
		for j in range(evens[i//2], evens[i//2 + 1] + 1):
			if(odd_row[j] < minimum):
				index = j
				minimum = odd_row[j]
		output_index.insert(i, index)
		#print(output_index)
	return output_index

def find_index_recur(item):
	n_rows = len(item)
	if(n_rows > 1):
		evens = find_index_recur(item[1:n_rows:2])
		output_index = find_subarray(item, evens)
		#print(output_index)
	else:
		output_index = [0]
		minimum = item[0][0]
		for i in range(0, len(item[0])):
			if item[0][i] < minimum:
				output_index[0] = i
				minimum = item[0][i]
	return output_index

items=[[10,17,13,28,23],[17,22,16,29,23],[24,28,22,34,24],[11,13,6,17,7],
[45,44,32,37,23],[36,33,19,21,6],[75,66,51,53,34]]
output =  find_index_recur(items)
print(output)

