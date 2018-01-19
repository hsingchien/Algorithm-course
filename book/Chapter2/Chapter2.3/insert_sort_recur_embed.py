import math
from merge_sort import merge_sort
def insert_sort_recur_embed(numbers):
	for i in range(1, len(numbers)):
		key = numbers[i]
		q = i - 1
		if key < numbers[q]:
			q = math.floor(q/2)
			while not (numbers[q] <= key and numbers[q + 1] >= key):
				if numbers[q] >= key and q != 0:
					# print("q,i", q, i)
					# print("[q]>=key ", numbers[q:q+2], key)
					q = math.floor(q/2)
					
				elif numbers[q+1] < key and q != 0:
					# print("q,i", q, i)
					# print("[q+1]<key ", numbers[q:q+2], key)
					q = math.floor((q + i)/2)
				elif q == 0:
					if numbers[q] > key:
						q = -1
						break
					else:
						q = 0
						break
			# print(q, i, key)
			numbers[q+2:i+1] = numbers[q+1:i]
			numbers[q+1] = key
			# print(numbers[0:])
	return numbers

A = [10,-2,3,4,3,5,2,9,8,-1,4,2,12,7,9,5]
B = A
A = insert_sort_recur_embed(A)
print(A)
merge_sort(B, 0, len(B))
print(B)