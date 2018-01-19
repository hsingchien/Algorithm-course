def insert_sort(numbers):
	for i in range(1, len(numbers)):
		key = numbers[i]
		while i >= 1 and numbers[i-1] < key:
			numbers[i] = numbers[i-1]
			i = i - 1
		numbers[i] = key
	return numbers

def mysearch(input_list, key):
	output_index = []
	i = len(input_list) - 1
	while i >= 0:
		if input_list[i] == key:
			output_index.append(i)
		i -= 1
	return output_index

def binary_add(biA, biB):
	n = len(biA)
	addup = 0
	result = []
	for i in range(n-1, -1, -1):
		if biA[i] + biB[i] + addup >= 2:
			result.insert(0, biA[i] + biB[i] + addup - 2)
			addup = 1
		else:
			result.insert(0, biA[i] + biB[i] + addup)
			addup = 0
	result.insert(0, 1)
	return result


def select_sort(numbers):
	for k in range(0, len(numbers)-1):
		temp = numbers[k]
		ind = k
		for j in range(k + 1, len(numbers)):
			if numbers[j] < temp:
				temp = numbers[j]
				ind = j
		numbers[ind] = numbers[k]
		numbers[k] = temp
	return numbers