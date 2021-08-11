from typing import List, Any, Tuple

import os
import pandas as pd
import numpy as np
from numpy import float64

lista = ['Joker_2009.xlsx', 'Joker_2010.xlsx', 'Joker_2011.xlsx', 'Joker_2012.xlsx', 'Joker_2013.xlsx',
         'Joker_2014.xlsx', 'Joker_2015.xlsx', 'Joker_2016.xlsx', 'Joker_2017.xlsx', 'Joker_2018.xlsx',
         'Joker_2019.xlsx', 'Joker_2020.xlsx', 'Joker_2021.xlsx']

# select file by user
try:
    print('Enter a number from 0 to 12 to select a file: ')
    answer = int(input())
    print(lista[answer])
except:
    print('Not a valid number!!!')

df = pd.read_excel(lista[answer])

### GET THE INPUT NUMBERS ####
nums = []
i = 1
while i < 6:
    print("Enter the number that you want to search.")
    try:
        ans = int(input())
        if not 1 <= ans <= 45:
            raise ValueError()
    except ValueError:
        print('Please enter a valid number!!!')
    else:
        nums.append(ans)
        i += 1

print(f"You entered the numbers : {nums} ")


# print(list(df.columns))
# print(df[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4','Unnamed: 5', 'Unnamed: 6']][2:]) # prints the rows we desire
# print(df['Unnamed: 9'][2:]) # prints complete successes column
### print(type(df.columns[9]))


### FIND THE OCCURENCES OF SUCCESS ###
def sucs(dataframe):
    col = 'Unnamed: 9'
    ans = dataframe.loc[dataframe[col] == 1]
    return ans[0:7]


### print(sucs(df))

### CREATE A NEW DATAFRAME WITH DATES AND JOKER NUMBERS ###
newdf = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:]
# print(newdf.shape) PRINTS THE SHAPE OF DATAFRAME
### change column type to float64
newdf = newdf.astype({'Unnamed: 2': float64, 'Unnamed: 1': str})

### CREATE A DATAFRAME FROM JOKER NUMBERS ###
numsdf = df[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:]
at = numsdf.to_numpy()
at = at.astype('int')  # convert every element to integer
print(at.shape)  # returns the rows and columns of nums dataframe
# print(at.shape[1])
### m = at.to_dataframe(at, cols = ['1', '2', '3', '4', '5'])
### print(m)

### CALCULATE THE OCCURENCES OF EACH OF THE SELECTED NUMBERS AT EACH OF THE 5 POSITIONS ###4
occurences = np.count_nonzero(at == nums[0], axis=0)  # get the count of a value in array
occurences2 = np.count_nonzero(at == nums[1], axis=0)  # get the count of a value in array
occurences3 = np.count_nonzero(at == nums[2], axis=0)  # get the count of a value in array
occurences4 = np.count_nonzero(at == nums[3], axis=0)  # get the count of a value in array
occurences5 = np.count_nonzero(at == nums[4], axis=0)  # get the count of a value in array
### noccurences = np.count_nonzero(at == 2, axis=1)
print(f"The occurences of {nums[0]} are {occurences} ")
print(f"The occurences of {nums[1]} are {occurences2} ")
print(f"The occurences of {nums[2]} are {occurences3} ")
print(f"The occurences of {nums[3]} are {occurences4} ")
print(f"The occurences of {nums[4]} are {occurences5} ")


### print(occurences)
### print(noccurences)
# print(at[0:])


# a2 = (newdf['Unnamed: 2'].values == 1).sum()
# a3 = (newdf['Unnamed: 2'].values == 2).sum()
# a4 = (newdf['Unnamed: 2'].values == 3).sum()
# a5 = (newdf['Unnamed: 2'].values == 4).sum()
# a6 = (newdf['Unnamed: 2'].values == 5).sum()
# a7 = (newdf['Unnamed: 2'].values == 6).sum()
# a8 = (newdf['Unnamed: 2'].values == 7).sum()
# a9 = (newdf['Unnamed: 2'].values == 8).sum()
# a10 = (newdf['Unnamed: 2'].values == 9).sum()
# a11 = (newdf['Unnamed: 2'].values == 10).sum()
#
# print(f'Total 1s and 2s in 2nd column are {a2} ---- {a3}')
# print(f'Total 3s and 4s in 2nd column are {a4} ---- {a5}')
# print(f'Total 5s and 6s in 2nd column are {a6} ---- {a7}')
# print(f'Total 7s and 8s in 2nd column are {a8} ---- {a9}')
# print(f'Total 9s and 10s in 2nd column are {a10} ---- {a11}')


### CREATE A FUNCTION TO CALCULATE OCCURENCES PER POSITION IN DATAFRAME ###
def calc(col, dataframe):
    for i in range(1, 45):
        print(str(i) + "----" + str((dataframe[f'Unnamed: {col}'].values == i).sum()))


# calc(2, newdf)
# calc(3, newdf)
# calc(4, newdf)

# print((newdf['Unnamed: 2'].values == 1).sum())
# print((newdf['Unnamed: 2'].values == 2).sum())
# print((newdf['Unnamed: 2'].values == 3).sum())
# print((newdf['Unnamed: 2'].values == 4).sum())
# print((newdf['Unnamed: 3'].values == 4).sum())


### FIND HOW MANY NUMBERS FROM THE SELECTED ARE IN A DATAFRAME ROW ###
# def successes_per_row(frame, data = nums):
#     successes = []
#     for i in range(0,frame.shape[0]):

def ss_for_row(myarray, row):
    '''checks if the numbers you entered are in a row. ATTENTION order
    of numbers matters'''
    return any(np.allclose(row, x) for x in myarray)

if ss_for_row(at,nums):
    print('There is a PERFECT MATCH !!!')
else:
    print(f'The {nums} do not have a complete match...' )
# print(ss_for_row(at, nums))

def matches(myarray, data):
    ''' returns a list of tuples with successful matches and their positions in array '''
    m: List[Tuple[Any, int, int]] = []
    for i in range(0,myarray.shape[0]):
#        s = []
        for j in range(0,myarray.shape[1]):
            if myarray[i,j] in data:
#                s.append(myarray[i,j])
#                print(s)
#                if len(s) > 1:
                    m.append((myarray[i,j],i,j))
            else:
                pass
    print(m)
    print(f'The numbers you entered find matches in {len(m)} positions out of {myarray.shape[0]} * '
          f' {myarray.shape[1]} = {myarray.shape[0] * myarray.shape[1]} total numbers')

    return m

a = matches(at,nums)
print(a)

for i in range(0,len(a)-1):
    if a[i][1] == a[i+1][1]:
        print(a[i][0] ,' ' , a[i+1][0])
    else:
        pass

print(newdf.shape)
# print(newdf.head)