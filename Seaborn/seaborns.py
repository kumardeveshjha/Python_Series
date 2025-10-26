# Why Seaborn
 
#%%
import seaborn as sns
import numpy as np
import pandas as pd 


# Why Seaborn 
# -> Provides a layer of abstraction hence simpler to use 
# -> Better Aesthetics 
# -> More graphs Included 
# -> Popular to use 


# Seaborn Roadmap 

# types of functions 

# -> Figure level : These are the high level of the graphs 
# -> Axis Graphs : This is the lower graph 

#  Seaborn function type 

# 1. Relational           2. Distribution         3. Matrix plot            4. Matrix Plot            5. Regplot            6. Multi plots   


#%%

""" :::::::::: Scatter plot  :::::::::"""

# -> It is a axes lavel function  
tip = sns.load_dataset('tips')
tip 

# sns.scatterplot(tip,x='total_bill',y='tip')


# sns.relplot(tip,x='total_bill',y='tip')
#  it will plot a rectangular plot 

# use figure level function more than relplot 
# because figure level functions are the bigger than relplot(axes plots) becaue it consists the most relplot 
 

sns.relplot(tip,x='total_bill',y='tip',kind='scatter',hue='sex',style='time',size='size')


# here 'hue' parameter is used to determine other piece of information 
# it adds the legnend and color 
# style : one layer of info 
# size : it will represent the item size according topo the quantity 

#%%

"""::::::::::;Line plot ::::::::::;;;;"""

# It is a kind of scatter plot but when qwe want a continuous data flow we use 
import plotly as px

gap = px.data.gapminder()
gap 

# temp_df = gap[gap['country']=='India']

# sns.relplot(temp_df,x='year',y='lifeExp')

temp_def = gap[gap['country'].isin(['India','Pakistan','China'])]

temp_def

# sns.relplot(temp_def,x='year',y='lifeExp',hue='country',kind='line')

#  when we use figurelevel plot then the legend is outside the graph 
#  The axes level function has only control on the axes so it shows the level

sns.lineplot(data=temp_def,x='year',y='lifeExp',hue='country')


#%%

# Now checking with more continents country 

temp_def = gap[gap['country'].isin(['India','Brazil','Germany'])]

temp_def

sns.relplot(data=temp_def,x='year',y='lifeExp',hue='country',style='country',kind='line',size='continent')

# -> Here style: It givesa dditional info of the graph
#  here size meand the thickness or thinness of the line

""" ::::::::::::; Facet Plot ::::::::::::::::::::"""

#%%

# -> It helps making the multiple plots using a particular column 
# -> Here we use 'col/row' parameter
# -> it will also used to make grids 
# -> Facet: "This will work only with figure level functions"
# ->  It will not work with scatter plot and lineplot 
sns.relplot(data=tip,x='total_bill',y='tip',kind='scatter',col='sex',row='day')

gap

sns.relplot(gap,x='lifeExp',y='gdpPercap',kind='scatter',col='year')



""":::::::: Distribution Plot :::::::::::"""

#  
# 
#  
























# %%
