import pandas as pd
jobs = pd.read_excel('jobs.xlsx', names = ['weight','length'])
jobs['diff'] = jobs['weight']-jobs['length']
jobs_sorted = jobs.sort_values(by=['diff', 'weight'], ascending = [0,0])
jobs_sorted['complete'] = jobs_sorted['length'].cumsum()
jobs_sorted['weighted_complete'] = jobs_sorted['weight']*jobs_sorted['complete']
print(jobs_sorted['weighted_complete'].sum())
jobs['ratio'] = jobs['weight']/jobs['length']
jobs_sorted_2 = jobs.sort_values(by='ratio',ascending=0)
jobs_sorted_2['complete'] = jobs_sorted_2['length'].cumsum()
jobs_sorted_2['weighted_complete'] = jobs_sorted_2['weight']*jobs_sorted_2['complete']
print(jobs_sorted_2['weighted_complete'].sum())
