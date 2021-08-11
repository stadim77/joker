import pandas as pd

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

df = df[2:]

### FIND THE JOKER COLUMN ###
print(len(df['Unnamed: 7'])) # the total number of events or jokers

am = list(df['Unnamed: 7'])

print(am)


# print(am[:8]) # print the first 8 joker numbers from list
# print(int(am[3]) == 10)

### GET THE INPUT NUMBERS ####
# nums = []
# i = 1
# while i < 6:
#     print("Enter the number that you want to search.")
#     try:
#         ans = int(input())
#         if not 1 <= ans <= 20:
#             raise ValueError()
#     except ValueError:
#         print('Please enter a valid number!!!')
#     else:
#         nums.append(ans)
#         i += 1
#
# print(f"You entered the numbers : {nums} ")

### ENTER A NUMBER FOR THE JOKER EVENT ###
# print("Enter the number for the EVENT that you want to search.")
# try:
#     ans = int(input())
#     if not 1 <= ans <= len(df['Unnamed: 7']):
#         raise ValueError()
# except ValueError:
#     print('Please enter a valid number!!!')

#print(df.dtypes)

### FIND OCCURENCES OF JOKER ###
while True:
     print("Enter the joker number that you want to search.")
     try:
         ans = int(input())
         if not 1 <= ans <= 20:
             raise ValueError()
     except ValueError:
         print('Please enter a valid number!!!')
     else:
         break
         #nums.append(ans)
         #i += 1

# print(am.index(str(ans)))
# [print(i) for i, j in enumerate(am) if j == str(ans)] # prints the positions of joker

### FIND THE OCCURENCES OF JOKER NUMBER ###
jok = []
# Because some are strings [2009,2010] and rest are ints #
if answer > 1:
    [jok.append(i) for i, j in enumerate(am) if j == str(ans)]
    print(f'!!! The events that joker was equal to {ans} are {len(jok)} out of {len(am)} events!!!')
else:
    [jok.append(i) for i, j in enumerate(am) if j == ans]
    print(f'!!! The events that joker was equal to {ans} are {len(jok)} out of {len(am)} events!!!')



print(df.iloc[jok,1:2]) # prints the rows with thw selected joker number

#print(df.loc[df['Unnamed: 7'] == ans])
# mask = df['Unnamed: 7'] == ans
# print(df[mask])
#df['Unnamed: 7'].astype('int32').dtypes
# #pd.to_numeric(df['Unnamed: 7'])
# print(df.dtypes)
# print(df.loc[df['Unnamed: 7'] == int(ans)])
# print(df['Unnamed: 7'])

### FIND OCCURENCES IN ROWS ###

def Diff(li1, li2):
    '''returns the difference between two lists'''
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def cuts(dataframe,mun):
    ''' returns the number of exact matches'''
    ans = 0 # complete match
    fours = 0 # 4 numbers that match
    threes = 0 # 3 numbers that match
    twos = 0 # 2 numbers that match
    for i in range(len(dataframe)):
        a = list(map(int,list(dataframe.iloc[i,2:7])))
        if len(Diff(a,mun)) == 0:
            ans += 1
        elif len(Diff(a,mun)) == 2:
            fours += 1
        elif len(Diff(a,mun)) == 4:
            threes += 1
        elif len(Diff(a, mun)) == 6:
            twos += 1
        else:
            pass
    #print(ans,fours,threes,twos)
    print(f'Complete matches : {ans}, Four number matches : {fours}, Three number matches : {threes} and two number matches : {twos}')
    return (ans,fours,threes,twos)

#cuts(df,[10,18,19,4,29])
cuts(df,[3, 1, 28, 21, 19])
cuts(df,[38, 1, 28, 42, 41])

def rowbyrow(dataframe):
    '''find the common numbers between consecutive rows of dataframe'''
    ans = 0
    for i in range(len(dataframe)-1):
        a = list(map(int,list(dataframe.iloc[i,2:7])))
        b = list(map(int,list(dataframe.iloc[i+1,2:7])))
        if len(set(a) & set(b)) > 0:
            if len(set(a) & set(b)) > 1:
                print(f'Row {dataframe.iloc[i,0]} and row {dataframe.iloc[i+1,0]} share {(set(a) & set(b))}')
            ans += 1
        else:
            pass
    print(f'The lines that share common numbers are {ans} out of total {len(dataframe)} events')
rowbyrow(df)

def rowbysecondrow(dataframe):
    '''find the common numbers between consecutive rows of dataframe'''
    ans = 0
    for i in range(len(dataframe)-2):
        a = list(map(int,list(dataframe.iloc[i,2:7])))
        b = list(map(int,list(dataframe.iloc[i+2,2:7])))
        if len(set(a) & set(b)) > 0:
            if len(set(a) & set(b)) > 1:
                print(f'Row {dataframe.iloc[i, 0]} and row {dataframe.iloc[i + 2, 0]} share {(set(a) & set(b))}')
            #print(f'Row {dataframe.iloc[i,0]} and row {dataframe.iloc[i+2,0]} share {(set(a) & set(b))}')
            ans += 1
        else:
            pass
    print(f'The lines that share common numbers are {ans} out of total {len(dataframe)} events')

rowbysecondrow(df)

def rowbythirdrow(dataframe):
    '''find the common numbers between consecutive rows of dataframe'''
    ans = 0
    for i in range(len(dataframe)-3):
        a = list(map(int,list(dataframe.iloc[i,2:7])))
        b = list(map(int,list(dataframe.iloc[i+3,2:7])))
        if len(set(a) & set(b)) > 0:
            if len(set(a) & set(b)) > 1:
                print(f'Row {dataframe.iloc[i, 0]} and row {dataframe.iloc[i + 3, 0]} share {(set(a) & set(b))}')
            #print(f'Row {dataframe.iloc[i,0]} and row {dataframe.iloc[i+3,0]} share {(set(a) & set(b))}')
            ans += 1
        else:
            pass
    print(f'The lines that share common numbers are {ans} out of total {len(dataframe)} events')

rowbythirdrow(df)

def rowbyfourthrow(dataframe):
    '''find the common numbers between 4 "consecutive" rows of dataframe'''
    ans = 0
    for i in range(len(dataframe) - 4):
        a = list(map(int, list(dataframe.iloc[i, 2:7])))
        b = list(map(int, list(dataframe.iloc[i + 4, 2:7])))
        if len(set(a) & set(b)) > 0:
            if len(set(a) & set(b)) > 1:
                print(f'Row {dataframe.iloc[i, 0]} and row {dataframe.iloc[i + 4, 0]} share {(set(a) & set(b))}')
            # print(f'Row {dataframe.iloc[i,0]} and row {dataframe.iloc[i+3,0]} share {(set(a) & set(b))}')
            ans += 1
        else:
            pass
    print(f'The lines that share common numbers are {ans} out of total {len(dataframe)} events')

rowbyfourthrow(df)