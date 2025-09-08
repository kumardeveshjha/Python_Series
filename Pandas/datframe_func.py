#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%


marks = pd.DataFrame([
     [120,100,36],
     [100,90,18],
     [110,95,20],
     [90,80,12],
     [90,80,12]
],columns=['iq','marks','package'])

# marks


# values_coumts (both series and dataframe): Counts the frequency count of rows

# marks.value_counts()

ipl = pd.read_csv('dataset/ipl-matches.csv')

# Find which player has won most potm -> in fial and semifinal 

# ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()

# Toss decision plot


# ipl['TossDecision'].value_counts().plot(kind='pie')


(ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False)


#%%
### ---- sort_values(Series and Dataframe) --> ascending --> no_position --> inplace --> multiple columns 

movies = pd.read_csv('dataset/movies.csv')

# movies.sort_values('title_x',ascending=False)

# inplace parameter makes the data permanently store 

# sorting using multiple column 

# movies.sort_values(['year_of_release','title_x'],ascending=[True,False])


batsman = pd.read_csv("dataset/batsman_runs_ipl.csv")

## Rank function in Dtafra

batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)

# batsman.sort_values('batting_rank')


# sort_index (Series and Dataframes)

# marks = {
#      'math':90,
#      'python':95,
#      'JS':90,
#      'Hindi':100
# }

# new_marks = pd.Series(marks)
 
# new_marks.sort_index()


# movies.sort_index(ascending=False)


## --> set_index(dataframe) --> inplace 


# batsman
batsman.set_index('batter')

batsman


## reset_index
batsman.reset_index()

batsman


# how to reset the index without losing index 

batsman.reset_index().batsman.set_index('batting_rank')

















#%%
