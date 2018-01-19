import heap_pack
import numpy as np
class node:
	def __init__(self, na, ke):
		self.name = na
		self.key = ke
	def __lt__(self, other):
		return self.key < other.key
	def __le__(self, other):
		return self.key <= other.key
	def __gt__(self, other):
		return self.key > other.key
	def __ge__(self, other):
		return self.key >= other.key
	def __eq__(self, other):
		return self.key == other.key
	def print(self):
		print("name:", self.name, end='\t')
		print("key:", self.key)

class node_list:
	def __init__(self, nodes):
		self.list = nodes # nodes is a list of nodes
		self.pointer = np.arange(0,len(nodes)) # index 0 is useless
		for i in range(0,len(nodes)):
			self.pointer[nodes[i].name] = i # pointer i is the index of node i in the list
	def print(self):
		for i in range(0,len(self.list)):
			print(i,end=', ')
			self.list[i].print()


