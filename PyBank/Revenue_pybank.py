#!/usr/bin/env python
# coding: utf-8


# In[138]:


import os
import csv


# In[205]:


import warnings
warnings.filterwarnings("ignore")


# In[206]:


inputfile= os.path.join(".","Resources", "budget_data.csv")
inputfile


# In[304]:


previous_profit=0
total_month=0
total=0
monthly_changes=[]
total_months=[]

with open(inputfile,"r") as csvfile:
    budget=csv.reader(csvfile,delimiter=",")
    header=next(budget, None)
    #for row in csvreader:
    for row in budget:
        total_month += 1
        total_months.append(row[0])
        float_Profits_Losses= float(row[1])
        total += float_Profits_Losses
        current_profit= float(row[1])
        monthly_change=current_profit - previous_profit
        monthly_changes.append(monthly_change)
        previous_profit=current_profit
    monthly_changes = monthly_changes[1:]
    average=sum(monthly_changes)/(Total_Months - 1)
    increase=max(monthly_changes)
    decrease=min(monthly_changes)
    dateincrease=monthly_changes.index(increase)
    datedecrease=monthly_changes.index(decrease)
    
        
        
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" + " " + str(total_month))
    print("Total: " + "$" + str(Total))
    print("Average Change: " + "$" + str(average))
    print("Greatest Increase: " + str(total_months[dateincrease + 1]) + " $" + str(increase))
    print("Greatest Decrease: " + str(total_months[datedecrease + 1]) + " $" + str(decrease))
  
 
# In[ ]:


with open(budget_new, "w") as txt_file:
    txt_file.write(output)
    budget_new = os.path.join("..", "Resources", "budget_new.txt")


# In[ ]:




