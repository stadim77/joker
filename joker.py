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

# print(list(df.columns))
# print(df[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4','Unnamed: 5', 'Unnamed: 6']][2:]) # prints the rows we desire
# print(df['Unnamed: 9'][2:]) # prints complete successes column
print(type(df.columns[9]))


### FIND THE OCCURENCES OF SUCCESS ###
def sucs(dataframe):
    col = 'Unnamed: 9'
    ans = dataframe.loc[dataframe[col] == 1]
    return ans[0:4]


print(sucs(df))

### CREATE A NEW DATAFRAME WITH DATES AND JOKER NUMBERS ###
newdf = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:]
# print(newdf.shape) PRINTS THE SHAPE OF DATAFRAME
### change column type to float64
newdf = newdf.astype({'Unnamed: 2': float64, 'Unnamed: 1': str})

### CREATE A DATAFRAME FROM JOKER NUMBERS ###
numsdf = df[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']][2:]
at = numsdf.to_numpy()
print(at.shape)  # returns the rows and columns of nums dataframe
occurences = np.count_nonzero(at == 2)  # get the count of a value in array
print(occurences)


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
