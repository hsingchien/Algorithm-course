import random as rand
# rand.seed(a = 10)
def randsearch(seq, t):
	l = len(seq)
	i = rand.randrange(0,l)
	k = 1
	index = [i]
	while len(set(index)) < l and seq[i] != t :
		i = rand.randrange(0,l)
		index.append(i)
		print(index)
		print(len(set(index)))
		k += 1
	return [i,k]

a = list(range(8,10))
ls = randsearch(a, 7)
print(ls)