# Why Seaborn
 
#%%
import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

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

# 1. Relational (relplot : scatter plot an dline plot )
# 2. Distribution         
# 3. Matrix plot
# 4. Regplot            
# 5. Multi plots   


#%%

""" :::::::::: Scatter plot  :::::::::"""

# -> It is a axes lavel function  
tip = sns.load_dataset('tips')
tip 

# sns.scatterplot(tip,x='total_bill',y='tip')

# here we have relplot means relational plot 
sns.relplot(tip,x='total_bill',y='tip')


# use figure level function more than relplot 
# because figure level functions are the bigger than relplot(axes plots) becaue it consists the most relplot 
 

sns.relplot(tip,x='total_bill',y='tip',kind='scatter',hue='sex',style='time',size='size')

# here 'hue' parameter is used to determine other piece of information 
# it adds the legend and color 
# style : one layer of info 
# size : it will represent the item size according to the quantity 

#%%

""":::::::::: Line plot ::::::::::;;;;"""

# It is a kind of scatter plot but when we want a continuous data flow we use 
import plotly as px

gap = px.data.gapminder()
gap 

# temp_df = gap[gap['country']=='India']

# sns.relplot(temp_df,x='year',y='lifeExp')

temp_def = gap[gap['country'].isin(['India','Pakistan','China'])]

temp_def

sns.relplot(temp_def,x='year',y='lifeExp',hue='country',kind='line')

#  when we use figurelevel plot then the legend is outside the graph 
#  The axes level function has only control on the axes so it shows the level

sns.lineplot(data=temp_def,x='year',y='lifeExp',hue='country')


#%%

# Now checking with more continents and country 

temp_def = gap[gap['country'].isin(['India','Brazil','Germany'])]

temp_def

sns.relplot(data=temp_def,x='year',y='lifeExp',hue='country',style='country',kind='line',size='continent')

# -> Here style: It gives additional info of the graph
#  here size means the thickness or thinness of the line

""" :::::::::::: Facet Plot ::::::::::::::::::::"""

#%%

# -> It helps making the multiple plots using a particular column 
# -> Here we use 'col/row' parameter
# -> it will also used to make grids 
# -> Facet: "This will work only with figure level functions"
# -> It will not work with scatter plot and lineplot 

sns.relplot(data=tip,x='total_bill',y='tip',kind='scatter',col='sex',row='day')

gap

sns.relplot(gap,x='lifeExp',y='gdpPercap',kind='scatter',col='year')



""":::::::: Distribution Plots :::::::::::"""

#  Used For univariate data analysis (independent)
#  Used to find out the distribution of tha distribution
#  Range of the observation 
#  Central Tendency - mean, mode 
#  Is the data bimodel is there multiple peaks in the data
#  Are there outliers? 

# Plots under distribution plot 
# -> Histplot
# -> kdeplot()
# -> rugplot 

#  Figure level -> diplot()  use kind in this to make axes level plot 
#  axes level -> histplot -> kdeplot -> rugplot 

# ploting univariate histograph 


#%%
tip

# sns.histplot(data=tip, x='total_bill')

#  Using the figure level function 
# sns.displot(data=tip,x='total_bill',bin=)

# Bin parameter 
# sns.displot(data=tip,x='total_bill',bins=2)


# It’s also possible to visualize the distribution of a categorical variable using the logic of a histogram. 
# Discrete bins are automatically set for categorical variables


# sns.displot(data=tip,x='day',kind='hist')

# hue parameter

sns.displot(data=tip,x='tip',hue='sex')


#%%
titanic = sns.load_dataset('titanic')

titanic

sns.displot(data=titanic,x='age',kind='hist',element='step',hue='sex')


# faceting using col and row -> this will not wirk when using axes level function 
sns.displot(data=titanic,x='age',kind='hist',element='step',col='sex')



""" Kernal Density Estimation (KDE)Plot  """

#%%
# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate
# density-> density of probability
# It is more used then Histplot because it is continuous and can provide the middle values
# 

# sns.kdeplot(data=tip,x='total_bill')

# sns.displot(tip,kind='kde',x='total_bill')

# hue -> fill (To fill the area under the curve)

sns.displot(data=tip,kind='kde',x='total_bill',hue='sex')

# %%
# ::::::::::: RugPlot ::::::::

# Plot marginal distributions by drawing ticks along the x and y axes.
# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.
# it is used side by side with other graphs 


sns.kdeplot(data=tip,x='total_bill',hue='sex')
sns.rugplot(data=tip,x='total_bill')


""" Bivariate Histogram """

# Bivariate histogram
# A bivariate histogram bins the data within rectangles that tile the plot 
# and then shows the count of observations within each rectangle with the fill color

# %%
sns.displot(data=tip,kind='hist',x='total_bill',y='tip')
sns.displot(data=tip,kind='kde',x='total_bill',y='tip')



"""":::::::::::: Matrix Plot ::::::::::"""

# -> Heatmap
# -> Clustermap

#  Here is not any figure level function 

#%%
gap

# Now we wll convert this data into wide from long data 
# using pivot 

heat_df = gap.pivot(index='country',columns='year',values='lifeExp')


# plt.figure(figsize=(15,20))
# sns.heatmap(data=heat_df)


# Just for the european country 

europe = gap[gap['continent']== 'Europe']

EU_heat = europe.pivot(index='country',columns='year',values='lifeExp')

# plt.figure(figsize=(15,20))
# sns.heatmap(data=EU_heat)


# adding values as annotation 
# linewidth
# Cmap
# sns.heatmap(EU_heat,annot=True,cmap='viridis')
# plt.show()


# %%
# clustermap 
px.data.iris()
















# %%
