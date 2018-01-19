import pandas as pd
import numpy as np

node1 = []
node2 = []
cost = []
cdic = {} # save the list of each cluster
ndic = {} # clust each node belongs to
with open('test1.txt') as f:
	lines = f.readlines()
for i in lines:
	l = i.split(sep=' ')
	node1.append(int(l[0]))
	node2.append(int(l[1]))
	cost.append(int(l[2]))
points = pd.DataFrame({'node1':node1,'node2':node2,'cost':cost})
points_sorted = points.sort_values(by='cost')
for i in range(1,max(node2)+1):
	ndic[i] = i
	cdic[i] = [i]

while(len(cdic) > 4):
	ind = points_sorted.index[0]
	node1 = points_sorted.loc[ind,'node1']
	node2 = points_sorted.loc[ind,'node2']
	cost = points_sorted.loc[ind,'cost']
	points_sorted.drop(ind, inplace=True)
	# merge clusters
	clus1 = ndic[node1]
	clus2 = ndic[node2]
	if clus1 != clus2:
		clus1_list = cdic[clus1]
		clus2_list = cdic[clus2]
		if len(clus1_list) >= len(clus2_list):
			for i in clus2_list:
				ndic[i] = clus1
			clus1_list.extend(clus2_list)
			cdic[clus1] = clus1_list
			del cdic[clus2]
		else:
			for i in clus1_list:
				ndic[i] = clus2
			clus2_list.extend(clus1_list)
			cdic[clus2] = clus2_list
			del cdic[clus1]
	print(len(cdic))
cdist = {}
while(len(cdist) < 6):
	ind = points_sorted.index[0]
	node1 = points_sorted.loc[ind,'node1']
	node2 = points_sorted.loc[ind,'node2']
	clus1 = ndic[node1]
	clus2 = ndic[node2]
	if(ndic[node2] != ndic[node1] and (not clus2*clus1 in cdist.keys())):
		cdist[clus1*clus2] = points_sorted.loc[ind,'cost']
	points_sorted.drop(ind, inplace=True)
	print(len(cdist))
for i in cdist.keys():
	print(cdist[i])
	


