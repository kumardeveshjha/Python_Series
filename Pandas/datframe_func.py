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

marks


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
# batsman.set_index('batter')

# batsman


## reset_index
print(type(batsman.reset_index()))

# batsman



# how to reset the index without losing index 


#%%
# rename (only dataframe): it changes the name of the column 
movies.set_index('title_x')

movies.rename(columns={'imdb_id':'id','poster_path':'link','year_of_release':"Release Year"},inplace=True)
 
# movies

# changes the name of the indexes 

# movies.rename(index={''})


### Unique : It gives the uniue values 
### nunique : it gives the direct number of the unique values except nan 
temp = pd.Series([1,2,3,1,3,4,1,3,4,2,4,np.nan])


temp.unique()


ipl['Season'].unique().shape
ipl['Season'].nunique()


#%%

## isNull() checks the missing values gives the boolean 

students = {
    'name': ["Dev", "Dev Jha", "Devesh", "Devesh Kumar", None, "Devendra", None],
    'branch': ["CS", "DS", "CSE", 'AI-ML', None, 'BT', None],
    'college': ['IITD', 'IIITD', 'IITB', None, 'IIITH', 'GLBCTM', None],
    'cgpa': [None, 10.0, 7.8, 8.9, None, 9.5, 8.5],
    'package':[20,30,25,None,60,12,None]
}


students_data = pd.DataFrame(students)

# students_data
# students_data[students_data.isnull()]



## hasnans(series): check the missing values 



## If there are missing values then we can remove them 

## Dropna :: It removes the entire row if there is any single null value  

# students_data.dropna()

## it is not good way because me may loose data 

# students_data.dropna(how='any')




# students_data.dropna(how='all')  # jab tak sae column mei null nahi hai tab tak koi bhi row nahi delete hogi 


# students_data.dropna(subset=['name'])


# when we want to remove the multiple column 

# students_data.dropna(subset=['name','college'])


## FillNa (series + dataframe) : It is used when we don't want to remove the unavailable data and add some specific value to the missing data 


# students_data['name'].fillna('unkown')


# students_data['package'].fillna(students_data['package'].mean())
# students_data['name'].fillna(method = 'ffill')  # forward fill using previous value 


#%%
### Drop_duplicated  :: Used to remove duplicate values 

marks.duplicated()

temp = pd.Series([1,2,3,2,3,3,4,5,5])

temp.drop_duplicates()
temp.drop_duplicates(keep='first')

## Virat kohli last game in delhi question 


## Drop(Series and Dataframe) :: delete the rows or columns 

# Droping in series will lead to drop using the particular index

#Dropping the column 
# students_data.drop(columns=['college','cgpa'])
 

# Droping the rows 

# students_data['name'].drop(index=[0,1])


## :::: Apply 









#%%


