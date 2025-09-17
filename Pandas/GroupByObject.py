#%%
import numpy as np
import pandas as pd 

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

# def movie_ranking(group):
#    group['genre_Rank'] = group['IMDB_Rating'].rank(ascending=False)
#    return group


# print(genre.apply(movie_ranking))


# Normalized rating on the basis of group 

def normalized_rating(group):
      group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max()-group['IMDB_Rating'].min())
      return group

print(genre.apply(normalized_rating))









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

