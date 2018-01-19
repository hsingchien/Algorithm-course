import pandas as pd
import numpy as np
tmp = list()
with open('output.txt') as f:
	lines = f.readlines()
for i in range(0, len(lines)):
	st = lines[i]
	st = np.fromstring(st, dtype = int, sep = '\t')
	tmp.append(st)
tmp = np.array(tmp)
tmp=tmp[0,]
tmp = np.sort(tmp)
tmp=tmp[::-1]
print(tmp[0:10])