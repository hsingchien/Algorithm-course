	def __init__(self, i, l):
		self.weight = i
		self.list = l # this weight is composed by what initial weights...weights
	def __lt__(self, other):
		return self.weight < other.weight
	def __le__(self, other):
		return self.weight <= other.weight
	def __gt__(self, other):
		return self.weight > other.weight
	def __ge__(self, other):
		return self.weight >= other.weight
	def __eq__(self, other):
		return self.weight == other.weight
	def __add__(self, other):
		sl = self.list.copy()
		ol = other.list
		sl.extend(ol)
		return symbol(self.weight+other.weight, sl)