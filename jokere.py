from datetime import date

import pandas as pd
import numpy as np
from numpy import float64

lista = ['Joker_2009.xlsx', 'Joker_2010.xlsx', 'Joker_2011.xlsx', 'Joker_2012.xlsx', 'Joker_2013.xlsx',
         'Joker_2014.xlsx', 'Joker_2015.xlsx', 'Joker_2016.xlsx', 'Joker_2017.xlsx', 'Joker_2018.xlsx',
         'Joker_2019.xlsx', 'Joker_2020.xlsx', 'Joker_2021.xlsx']

df1 = pd.read_excel(lista[11])
df2 = pd.read_excel(lista[10])
df3 = pd.read_excel(lista[9])
df4 = pd.read_excel(lista[8])
df5 = pd.read_excel(lista[7])


#print(df1.columns)
#print(df.values)

newdf1 = df1[[ 'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2020','Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
newdf2 = df2[[ 'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2019','Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
newdf3 = df3[[ 'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2018','Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
newdf4 = df4[[ 'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2017','Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
newdf5 = df5[[ 'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2016','Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]

#print(newdf3.columns)


dtf1 = newdf1.rename(columns = {'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2020': 'eventid','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd', 'Unnamed: 4':'3rd','Unnamed: 5': '4th','Unnamed: 6': '5th', 'Unnamed: 7':'joker'})
dtf2 = newdf2.rename(columns = {'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2019': 'eventid','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd', 'Unnamed: 4':'3rd','Unnamed: 5': '4th','Unnamed: 6': '5th', 'Unnamed: 7':'joker'})
dtf3 = newdf3.rename(columns = {'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2018': 'eventid','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd', 'Unnamed: 4':'3rd','Unnamed: 5': '4th','Unnamed: 6': '5th', 'Unnamed: 7':'joker'})
dtf4 = newdf4.rename(columns = {'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2017': 'eventid','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd', 'Unnamed: 4':'3rd','Unnamed: 5': '4th','Unnamed: 6': '5th', 'Unnamed: 7':'joker'})
dtf5 = newdf5.rename(columns = {'ΑΠΟΤΕΛΕΣΜΑΤΑ ΤΖΟΚΕΡ 2016': 'eventid','Unnamed: 1':'date','Unnamed: 2':'1st','Unnamed: 3':'2nd', 'Unnamed: 4':'3rd','Unnamed: 5': '4th','Unnamed: 6': '5th', 'Unnamed: 7':'joker'})

### CREATE NEW DFs WITHOUT THE HEADERS ###
dtf11 = dtf1[2:]
dtf22 = dtf2[2:]
dtf33 = dtf3[2:]
dtf44 = dtf4[2:]
dtf55 = dtf5[2:]

# dtf11 = dtf11.astype({'date': date, 'eventid' : int} )
# dtf22 = dtf22.astype({'date': date, 'eventid' : int} )
# dtf33 = dtf33.astype({'date': date, 'eventid' : int} )
# dtf44 = dtf44.astype({'date': date, 'eventid' : int} )
# dtf55 = dtf55.astype({'date': date, 'eventid' : int} )

# dtf11['date'].astype('datetime64')
# dtf22['date'].astype('datetime64')
# dtf33['date'].astype('datetime64')
# dtf44['date'].astype('datetime64')

##print(dtf11.info)
# print(newdf1.head)
# print(newdf2.head)
# print(newdf3.head)

#print(newdf2[2:])

###frames = [dtf1[2:], dtf2[2:], dtf3[2:], dtf4[2:]]

### MERGE THE DFs ###
frames = [dtf11, dtf22, dtf33, dtf44, dtf55]

total = pd.concat(frames) # keys = ['x','y','z','d']

#print(total.loc['x'])
print(total.shape)
# print(total.dtypes)
### change column data types ###
#total.astype({'eventid' : int64,'1st': int64,'2nd' : int64, '3rd' : int64, '4th' : int64, '5th' : int64, 'joker' : int64})
# total['eventid'].astype('int')
###print(total.head)

# print(total.filter(items=[1,40],axis=0))

### AN ALTERNATIVE WAY TO ADD DATAFRAMES ###
result = dtf1[2:].append(dtf2[2:], )
res = result.append(dtf3[2:],ignore_index = True)
# print(newdf1[2:].shape)
# print(newdf2[2:].shape)
# print(newdf3[2:].shape)


print(res.shape)
total = total.astype({'1st':int}, copy=True)
### FILTER ROWS BY CONDITIONS ###
sample = total[total['2nd'] > 10]
sample2 = total[(total['1st'] == 18) & (total['2nd'] == 7) & (total['3rd'] == 37)]
print(sample2.shape[0])

am = [19,]
sample3 = total[total['1st'].isin(am)]
sample4 = total[total['2nd'].isin(am)]
sample5 = total[total['3rd'].isin(am)]
sample6 = total[total['4th'].isin(am)]
sample7 = total[total['5th'].isin(am)]

print(sample3.shape[0]) # returns the number of rows that match selected criteria
print(sample4.shape[0]) # returns the number of rows that match selected criteria
print(sample5.shape[0]) # returns the number of rows that match selected criteria
print(sample6.shape[0]) # returns the number of rows that match selected criteria
print(sample7.shape[0]) # returns the number of rows that match selected criteria

#print(res.head)
print(sample.shape)
print((sample))
### CREATE A FUNCTION TO FIND MATCHES IN DATAFRAME ###
# def comple(dataframe, nums, cols):
#     if (dataframe[cols[0]]==nums[0]) & (dataframe[cols[1]]==nums[1]) & (dataframe[cols[2]]==nums[2]):
#         if (dataframe[cols[3]])==nums[3]:
#             print("Well done!!! 4 matches")
#         else:
#             print("You get 3 matches in a row")
#         if (dataframe[cols[4]]==nums[4]):
#             if (dataframe[cols[5]]==nums[5]):
#                 print("GREAT!!! SUCCESS!!! JOKER!!!")
#             else:
#                 print("YYYYou get 5 in a row!!!!")
#
# colu = ['1st','2nd','3rd','4th','5th','joker']
# comple(total,[12,39,40,5,27,1],colu)

### SAVE RES TO CSV FILE ###
res.to_csv('res.csv',index = False, index_label=False)
total.to_csv('total.csv',index = False, index_label=False)
