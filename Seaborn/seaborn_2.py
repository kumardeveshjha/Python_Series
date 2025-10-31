
# %%
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px 

# Categorical plot 

# -> Categorical Scatter Plot
#    1. Swarmplot
#    2. Stripplot

# -> Categorical Distribution Plot
#    1. Boxplot
#    2. Violinplot

# -> Categorical Estimation Plots 
#    1.Barplot 
#    2.Pointplot 


tip = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# %%
""":::::::::::::::: Catagorical Plots ::::::::::::::::::::"""

# When you want to check distribution of categorical column with respect to a numerical column

# Strip plot 
# This is the axes level function 

sns.stripplot(data=tip,x='day',y='total_bill')
# here seaborn adds some of the noise 
# to remove this we use jitter p

sns.stripplot(data=tip,x='day',y='total_bill',jitter=False)

# using figure level function 
# catplot

sns.catplot(data=tip,x='day',y='total_bill',kind='strip',hue='sex')

# swarnplot 
# it is good for small dataset
sns.catplot(data=tip,x='day',y='total_bill',kind='swarm')

# *-> Bivariate analysis 


""":::::::::::: Categorical Distribution Plot """


# -> These are used to analysis of single variable 

# BOXPLOT 

# A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile [Q1], median, third quartile [Q3] and “maximum”). 
# It can tell you about your outliers and what their values are. Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and if and how your data is skewed.

# %%
# sns.catplot(data=tip,x='sex',y='total_bill',kind='box')
# sns.catplot(data=tip,x='day',y='total_bill',kind='box')

# hue
# sns.catplot(data=tip,x='day',y='total_bill',kind='box',hue='sex')

# Total boxplot of the entire column -> numerical col
# sns.catplot(data=tip,y='total_bill',kind='box')


# Voiline plot (Box plot + KDE Plot)

sns.violinplot(data=tip,x='day',y='total_bill',cmap='viridis')

# Using figure plot
sns.catplot(data=tip,x='day',y='total_bill',cmap='viridis',kind='violin',hue='sex')


""":::::::::Categorical Estimate Plot (Central Tendancy ) :::::::::::::;"""
# There sre used to plot the estimated analysis 

# %%
# -> Bar PLot:


# sns.barplot(data=tip,x='sex',y='total_bill',errorbar=None,hue='smoker')

# errorbar to remove error bar

#  hue on smaoker
# estimator  to do some statical values like mean mode or sd

#  Point Plot 

# it gives the difference of the differnce between the categories 
sns.pointplot(data=tip,x='sex',y='total_bill',errorbar=None,hue='smoker')

# When there are multiple observations in each category, it also uses bootstrapping to compute a confidence interval around the estimate, 
# which is plotted using error bars


# Countplot 

# A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable
# just like pandas values_count it also gives the number 
# it takes only one parameter or column
sns.catplot(data=tip,x='sex',kind='count')
sns.catplot(data=tip,x='sex',kind='count',hue='day')

# faceting in the categorical plots 

sns.catplot(data=tip,x='sex',y='total_bill',col='smoker',row='time',kind='box')


"""::::::: Regression Plots :::::::::::::::::::::;;"""
# -> This plot is used to plot the mathematical relationship between one quantity to another quantty 

# -> This helps to plot a linear regression graph 
# -> and plots a regression line 
# regplot
# lmplot
# In the simplest invocation, both functions draw a scatterplot of two variables, x and y, and then fit the regression model y ~ x and plot the resulting regression line and a 95% confidence interval for that regression.

# %%
tip
# regplot 
# It does not upport the hue parameter 
# sns.regplot(data=tip,x='tip',y='total_bill')

# lmplot -> It is a figure level function 
# It supports hue parameter 
# sns.lmplot(data=tip,x='tip',y='total_bill',hue='sex')

# residual plot 
sns.residplot(data=tip,x='tip',y='total_bill')



"""::::::::::::: Multi Gridplot ::::::::::::::::"""

#%%
###### -> FacetGrid 

#  Secomnd way to draw a facet plots and it gives more flexibility 
# sns.catplot(data=tip,x='sex',y='total_bill',kind='violin',hue='sex',col='day',row='time')



# using facetgrid 
# 
# g = sns.FacetGrid(data=tip,col='day',row='time')
# g.map(sns.violinplot,'sex','total_bill')
# it helps to plot more customized plots but we will not using this 99% times 

# -> Pair Plot 
#  it plots the relationship pairwise between numeric columns 
iris
# sns.pairplot(iris,hue='species')

#  it gives the bar/kde plot on diagonal because they are betweeen same quantity 
# between different columns it gives scatter plot 


# -> pairgid

# this is like parent of the pairplot 

# g = sns.PairGrid(data=iris,hue='species')
# g.map(sns.scatterplot)

# here we have more flexibility over diagram 

# g = sns.PairGrid(data=iris,hue='species')

# g.map_diag(sns.violinplot)
# g.map_offdiag(sns.kdeplot)



# making different graph around the diagonal 

g = sns.PairGrid(data=iris,hue='species')
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)
g.map_diag(sns.histplot)


# Jointgrid and Jointplot 

# This is used when we want to do analysis univariable and multivariable 
# This provides the analysis of univariate and multivariate
# in this plot we use a single type of graph 

# %%
# sns.jointplot(data=tip,x="total_bill",y='tip',kind='kde')



# jointgrid 

# it provides the multi graphs analysis with two different plots side by side 

g = sns.JointGrid(data=tip,x='total_bill',y='tip')
g.plot(sns.scatterplot,sns.violinplot)


#%%
# dataset in seaborn 

sns.get_dataset_names()

# load the data set 
sns.load_dataset('seaice')
# %%
