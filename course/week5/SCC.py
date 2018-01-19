import pandas as pd
import numpy as np
from DFS import DFS_loop


sc_net  = pd.read_table('SCC.txt', header = None, delimiter=" ",dtype = 'float64'
	,names = ['tail','head','none'])
sc_net = sc_net.iloc[:,0:2]
sc_net = sc_net.astype(np.int64)

sc_net_c = sc_net.copy()
sc_net_c.columns = ['head','tail']
scc_first = DFS_loop(sc_net)
f_time = scc_first[0]
ft = np.copy(f_time)
scc_second = DFS_loop(sc_net_c, ft)
leaders = scc_second[1]
scc_count = np.bincount(np.int64(leaders))
scc_count = scc_count[np.nonzero(scc_count)]
print(scc_count)
np.savetxt('output.txt',scc_count,fmt="%.0i",delimiter=",",newline="\t")