#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import csv


# In[20]:


import us_state_abbrev as usabb
from datetime import datetime


# In[70]:


employee_data = os.path.join("employee_data.csv")
with open(employee_data,"r") as file, open('new_employee_data.csv', 'w') as writer:
    csv_reader_employee = csv.reader(file, delimiter=",")
    next(csv_reader_employee,None)
    writer.write('Emp ID,First Name,Last Name,DOB,SSN,State')
    for row in csv_reader_employee:
        writer.write('\n')
        new_row = [row[0]]
        new_row += row[1].split()
        new_row.append(datetime.strptime(row[2], "%Y-%m-%d").strftime('%d/%m/%Y'))
        new_row.append('***-**-' + row[3].split('-')[-1])
        new_row.append(usabb.us_state_abbrev.get(row[4]))
        writer.write(','.join(new_row))

