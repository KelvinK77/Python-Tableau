# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 01:55:07 2023

@author: kelvin
"""

import json 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique value for the purpose column
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#working with arrays
#1D array
arr = np.array([1,2,3,4])

#0D array
arr = np.array(43)
 
#@D array
arr = np.array([[1,2,3,], [4,5,6]])

#working with if statemants

a = 40
b = 500

if b > a:
    print('b is greater than a')

#let add more conditions

a = 40
b = 500
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')

#what if a condition is not met?

a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('No conditions met')

#another condition diffrent metrics

a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No conditions met')
    
#Using or
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
else:
    print('No conditions met')    
    
#fico score

fico = 250

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'very poor'
elif fico >= 400 and fico < 600:
    ficocat = 'poor'
elif fico >= 601 and fico < 660:
    ficocat = 'fair'
elif fico >= 660 and fico < 700:
    ficocat = 'good'
elif fico >= 700:
    ficocat = 'excellent'
else:
    ficocat = 'unknown'
print(ficocat)     

#for loops

fruits = ['apple', 'mango', 'pear', 'cherry']

for x in fruits:
    print(x)
    y = x+' fruits'
    print(y)
    
for x in range(0,3):
    y = fruits[x]+' for sale'
    print(y)
    
#applying for loops to loan data

#using first 10

lenght = len(loandata)
ficocat = []
for x in range(0,lenght):
    category = loandata ['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'very poor'
        elif category >= 400 and category < 600:
            cat  = 'poor'
        elif category >= 601 and category < 660:
            cat  = 'fair'
        elif category >= 660 and category < 700:
            cat  = 'good'
        elif category >= 700:
            cat = 'excellent'
        else:
            cat = 'unknown'  
    except:
        cat = 'unknown'
    ficocat.append(cat)    
 
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat  
  
#df. loc as conditional statements
#df.loc[df[columnname] condition, new columnname] = 'value if th condition is met'

#for intrest rate, a new column is wanted. rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] >0.12, 'int.rate.type'] = 'high'
loandata.loc[loandata['int.rate'] <=0.12, 'int.rate.type'] = 'low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'orange' , width = 0.1)
plt.show()



purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'brown' , width = 0.2)
plt.show()

#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint, color = 'orange')
plt.show()

#writing to csv

loandata.to_csv('loan_cleaned.csv' , index = True)



        




































    
    
    
    
    
    
    
    
    



















































