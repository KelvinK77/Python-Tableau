# -*- coding: utf-8 -*-
"""
Created on Thu May 25 02:34:00 2023

@author: kelvi
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv 

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv' , sep=';')

#summary of the data
data.info()

#working with calculations

#Defining variables

costperitem = 11.73
sellingpriceperitem = 21.11
numberofitems = 6

#Mathematical operation on Tableu

profitperitem = 21.11 - 11.73
profitperitem = sellingpriceperitem - costperitem

profitpertransaction = numberofitems * profitperitem

costpertransaction = numberofitems * costperitem

sellingpricepertransaction = numberofitems * sellingpriceperitem

#costpertransaction collum calculation

#costpertransaction = costperitem * numberofitems
#variable = datafrane ['column_name']

costperitem = data['CostPerItem']

numberofitems = data['NumberOfItemsPurchased']

costpertransaction = costperitem * numberofitems

#adding a new column to a dataframe

data['costpertransaction'] = costpertransaction

#sales per transaction

data['salespertransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation = cales - cost

data['profitpertransaction'] = data['salespertransaction'] - data['costpertransaction']

data['markup'] = (data['salespertransaction'] - data['costpertransaction'] )/data['costpertransaction']

#Rounding Markup

roundmarkup = round(data['markup'], 2)

data['markup'] = round(data['markup'], 2)

#combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#checking columns type
day = (data['Day'].dtype)

#change column type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] # brings all rows on the 2nd column

data.iloc[4,2] #brings 4th row, 2nd column

#Using split to split the client_keywords fields

#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new column for the splits column in client keyword

data['clientage'] = split_col[0]
data['clienttype'] = split_col[1]
data['lenghtofcontract'] = split_col[2]
#using the replace function

data['clientage'] = data['clientage'].str.replace('[' , '')

data['lenghtofcontract'] = data['lenghtofcontract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files

#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#medging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)

data = data.drop('Day' , axis = 1 )

data = data.drop(['Year' , 'Month'], axis = 1)

#export into a csv

data.to_csv('ValueInc_cleaned.csv', index = False)













































