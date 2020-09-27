#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv


# In[3]:


budget_data = os.path.join("Resources", "budget_data.csv")


# In[10]:


def average(changes):
    result = sum(changes)/len(changes)
    return (f'Average Change: ${result}')


Total = 0
numbers =[]
months = []
changes = []

with open(budget_data,"r") as file:
    csv_reader_budget = csv.reader(file, delimiter=",")
    next(csv_reader_budget, None) 
    for row in csv_reader_budget:
        Total += float(row[1])
        numbers.append(int(row[1]))
        months.append(row[0])
        
changes = [int(numbers[n])-int(numbers[n-1]) for n in range(1,len(numbers))]  
months_max = months[changes.index(max(changes))+1]
months_min = months[changes.index(min(changes))+1]


print("Financial Analysis\n")
print('--------------------------\n')
print(f'Total Month: {len(months)}\n')
print(f'Total: {int(Total)}\n')   
print(average(changes))
print(f'\nGreatest Increase in Profits: {months_max} (${max(changes)})\n')
print(f'Greatest Decrease in Profits: {months_min} (${min(changes)})')


# In[14]:


with open("PyBank_result.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write('--------------------------\n')
    file.write(f'Total Month: {len(months)}\n')
    file.write(f'Total: {int(Total)}\n') 
    file.write(average(changes))
    file.write(f'\nGreatest Increase in Profits: {months_max} (${max(changes)})\n')
    file.write(f'Greatest Decrease in Profits: {months_min} (${min(changes)})')


# In[ ]:




