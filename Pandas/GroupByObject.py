#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# here we will learn about the group by object 

# GroupBy always applied at categorical data 

movies = pd.read_csv('dataset/imdb-top-1000.csv')
movies


genre = movies.groupby('Genre')

# Find the numnber of movies done by actors 

# actor = movies.groupby('Star1')
# actor['Series_Title'].count().sort_values(ascending=False)

#:::::::: in most of the cases (90% )
#---> 1. GroupBy Object --> Desired Column  --> Aggregate Operation on that column (Sum, min ,Max, std, count, average)
# movies.info()



#%%

# Find Total Number of groups -> len
## Using Len 

# len(movies.groupby('Star1'))


## Find Each items in each group -> size 
# this can be done using value_count()
# genre.size()


## first()/last() -> nth item 
# genre.first()
# genre.last()
# genre.nth(5)

## get_group --> vs filtering 

# This gives the particular group of the groupBy 

# genre.get_group('Horror')


## groups (barely used: It gives the index position of the groupby Data)

# genre.groups

## describe 

# genre.describe()

## sample :::>>>>>>>>. Gives the randomly data from groups 

# genre.sample()

# genre.sample(2,replace=True)

##  nunique 

# genre.nunique() #means unique values on the basis of column and groups 


#%%

## Aggregate Method

# genre.sum()

# genre.agg(
     
#      {
#           'Runtime':"mean",
#           'IMDB_Rating':"mean",
#           "No_of_Votes":"sum",
#           'Gross':'sum',
#           'Metascore':'min'
          
#      }
# )


## Passing the list in the aggregator 

# genre.agg(['min','max','sum'])


## Merging the syntax 

# genre.agg(
     
#      {
#           'Runtime':['min','max','sum','mean'],
#           'IMDB_Rating':['min','max','mean'],
#           "No_of_Votes":['min','max','sum','mean'],
#           'Gross':'sum',
#           'Metascore':'min'
          
#      }
# )



#%%
## Loop on the groupBy objects 

# for group,data in genre:
     # data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]

# df = pd.DataFrame(columns=movies.columns)
# for group,data in genre:
#      df = df._append(data[data['IMDB_Rating'] == data['IMDB_Rating'].max()])

# print(df)


## :::::::::::::: apply()--> can make our custom function or logic 

# split(using groupByObject)--> apply(transformation apply) --> combine(data )

# Find the number of movies in the group that are started with 'a'

# def foo(group):
#    return group['Series_Title'].str.startswith('A').sum()

# print(genre.apply(foo,include_groups=True))

# Find ranking of each movie in the group according to IMDB score

def movie_ranking(group):
   group['genre_Rank'] = group['IMDB_Rating'].rank(ascending=False)
   return group


print(genre.apply(movie_ranking))


# Normalized rating on the basis of group 

def normalized_rating(group):
      group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max()-group['IMDB_Rating'].min())
      return group

print(genre.apply(normalized_rating))


## GroupBy on Multiple columns 

#%%
duo = movies.groupby(['Star1','Director'])
duo

duo.size()
duo.get_group(('Amole Gupte','Aamir Khan'))


# Find the combo of actor and director most earn 


duo['Gross'].sum().sort_values(ascending=False)


# Actor with their best genre perpformance on the basis of average metascore 
movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False)

# Aggregate on multiple colums

# print(duo.agg(['min','max','mean']))


### Practice on the Grop By Object Complex Problems 


#%%
ipl = pd.read_csv('dataset/deliveries.csv')

ipl.head(1)

# find the top 10 batsman in terms of runs 

# ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)


# find the batsman with max no. of sixes 

# sixes = ipl[ipl['batsman_runs'] == 6]

# sixes.groupby('batsman')['batsman'].count().sort_values(ascending=False)
  
# find batsman with most of 4's and 6's in last 5 overs 

# ipl[ (ipl['batsman_runs'] ==6 )| (ipl['batsman_runs']== 4)]


last_overs = ipl[ipl['over'] > 15]

# temp = last_overs[(last_overs['batsman_runs'] == 6) | (last_overs['batsman_runs'] == 4)]
# temp
# temp.groupby('batsman').size().sort_values(ascending=False).head(5)



# Find Virat kohli's record against all teams 

temp_df =ipl[ipl['batsman'] == 'V Kohli']
temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index()


# Create a function that can return the highest score of any batsman 

temp_run = ipl[ipl['batsman'] == 'V Kohli']

temp_run.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

def high_score(batsman):
      temp_run = ipl[ipl['batsman'] == batsman]
      return temp_run.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]
      
      
high_score("MS Dhoni")
































# 
# Series_Title
# 
# Released_Year
# 
# Runtime
# 
# Genre
# 
# IMDB_Rating
# 
# Director

















# %%

