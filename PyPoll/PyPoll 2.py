#!/usr/bin/env python
# coding: utf-8

# In[110]:


import os
import csv


# In[111]:


election_data = os.path.join("Resources", "election_data.csv")


# In[127]:


elections = {}
total_voters = 0
results = []

with open(election_data,"r") as file:
    csv_reader_election = csv.reader(file, delimiter=",")
    next(csv_reader_election, None)
    for row in csv_reader_election:
        elections[row[2]] = elections.get(row[2], 0) + 1
        total_voters = sum(elections.values())
        win_candidate = max(elections,key=elections.get)
to_print = ['Election Results']
to_print.append(f'Total Votes: {total}')

for k,v in elections.items():
    results.append('{}: {:.3%} ({})'.format(k,v/total,v))
to_print.append('\n'.join(results))
to_print.append('Winner:{}'.format(win_candidate))  
for x in to_print:
    print(x)
    print('----------------------------')


# In[ ]:




