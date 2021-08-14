from jokerApp import nums, year , joker, files
import pandas as pd


lista = ['Joker_2009.xlsx', 'Joker_2010.xlsx', 'Joker_2011.xlsx', 'Joker_2012.xlsx', 'Joker_2013.xlsx',
         'Joker_2014.xlsx', 'Joker_2015.xlsx', 'Joker_2016.xlsx', 'Joker_2017.xlsx', 'Joker_2018.xlsx',
         'Joker_2019.xlsx', 'Joker_2020.xlsx', 'Joker_2021.xlsx']

# print(nums)
#print(year)
#print(joker)

df = pd.read_excel(year[0])

df = df[2:]

### THIS IS THE JOKER NUMBER COLUMN ###
am = list(df['Unnamed: 7'])

### get the index of file in lista ###
answer = lista.index(year[0])
# print(answer)

ans = joker[0]

### FIND THE OCCURENCES OF JOKER NUMBER ###
jok = []
# Because some are strings [2009,2010] and rest are ints #
if answer > 1:
    [jok.append(i) for i, j in enumerate(am) if j == str(ans)]
    print(f'!!! The events that joker was equal to {ans} are {len(jok)} out of {len(am)} events!!!')
else:
    [jok.append(i) for i, j in enumerate(am) if j == ans]
    print(f'!!! The events that joker was equal to {ans} are {len(jok)} out of {len(am)} events!!!')

### PRINT THE DATES THAT THE SELECTED JOKER OCCURED ###
print(df.iloc[jok,1:2]) # prints the rows with thw selected joker number

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

cuts(df,nums)

def rowbyrow(dataframe):
    '''find the common numbers between consecutive rows of dataframe'''
    ans = 0
    mynums = set() # create a set to add common numbers
    for i in range(len(dataframe)-1):
        a = list(map(int,list(dataframe.iloc[i,2:7])))
        b = list(map(int,list(dataframe.iloc[i+1,2:7])))
        if len(set(a) & set(b)) > 0:
            if len(set(a) & set(b)) > 1:
                #mynums.add(set(a)[0])
                #mynums.add(set(b)[0])
                print(f'Row {dataframe.iloc[i,0]} and row {dataframe.iloc[i+1,0]} share {(set(a) & set(b))}')
                mynums.update((set(a) & set(b)))
            ans += 1
        else:
            pass
    print(f'The lines that share common numbers are {ans} out of total {len(dataframe)} events')
    print(mynums)
rowbyrow(df)