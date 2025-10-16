# Fundamentals of Matplotlib 

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


## 2D Line Plot 

# When to use 
# 1. Bivariate Analysis 
# 2. Categorical -> numerical and numerical -> numerical 
# 3. Use case - Time series data 


# ploting a simple function 


price = [48000,54000,57000,49000,45000]
year= [2020,2021,2022,2023,2024]

# plt.plot(year,price)
# plt.show()


#%%
# ploting the runs of virat and rohit career ipl 

batsman = pd.read_csv('Dataset/sharma-kohli.csv')
batsman

plt.plot(batsman['index'],batsman['V Kohli'],color='red',label='Kohli',marker='+',markersize='small')
plt.plot(batsman['index'],batsman['RG Sharma'],label='Rohit',color='Blue',marker='D')

# # title of the graph

# plt.title('Rohit Sharma Vs Virat Kohli Career Comparioson')

# #providing xlebel 
# plt.xlabel('Season')
# # providing y lebel
# plt.ylabel('Runs')

# changing the view of the line 
# using linestyle --> Changing the type of the line 
# linewidth  --> to make line's width 
# also can change the points --> using 'marker'
# can change the marker size using --> 'markersize'

# legend --> Naming the line 

# using lebel we can give the name to the lines 
# to show on screen we use ->

plt.legend(loc='best')   #it will automatically figuredit out 
plt.grid()
plt.show()

#%%

# when there is anomoly in the graph due to outlier data 
# we can set the limit (trim the graph)

# price = [48000,54000,57000,49000,4500000]
# year= [2020,2021,2022,2023,2024]

# plt.plot(year,price)

# # when there is anomoly in the graph due to outlier data 
# # we can set the limit (trim the graph)
# plt.ylim(0,75000)
# plt.xlim(2020,2023)


# Grid 

plt.plot(batsman['index'],batsman['V Kohli'],color='red',label='Kohli')
plt.plot(batsman['index'],batsman['RG Sharma'],label='Rohit')


plt.title('Rohit Sharma Vs Virat Kohli Career Comparioson')
plt.xlabel('Season')
plt.ylabel('Runs')
plt.grid()  # adds the grid in the graph 


# show --> to plot the graph 


#%%
### Scatterplot ::::::::
# -> Bivariate Analysis
# -> Numerical vs Numerical (only favourable)
# -> Use Case - Finding the correlation. 


# x = np.linspace(-10,10,50)

# y = 200*x + 4  #+np.random.randint(0,300,50)
# y 


# plt.scatter(x,y)

# df = pd.read_csv('Dataset/batter.csv')

# df = df.head(50)

# plt.scatter(df['avg'],df['strike_rate'],color='red')

# plt.title('Avg and strike rate analysis of top players')

# plt.xlabel('Average')
# plt.ylabel('Strike-Rate')
# plt.legend(loc='best')

##  Size : Tjis is used to check the correlation between the labels 

tips = sns.load_dataset('tips')

plt.scatter(tips['total_bill'],tips['tip'],s=tips['size']*10)


#%%
## scatterplot without using scatterplot

## --> This is faster technoique 
plt.plot(tips['total_bill'],tips['tip'],'o')


# Scatterplot vs plot --> Scatterplot is used for small data vizualization and is slower than plot

## Bar Graph 
# -> Bivariate Analysis 
# -> Numerical vs categorical 
# -> Use case- Aggregate analysis of groups 


#%%

# dev = pd.DataFrame([20,30,10,50,80],index=['white','red','yellow','green','blue'],columns=['children'])

# dev.plot(kind='bar')

color = ['Green','Red','Blue','Yellow','White']

children = [100,200,280,150,500]

plt.bar(color,children,color='Red')

plt.xlabel('color')
plt.ylabel('children')


# we can also make it horizontally using plot.barh()


#%%

df= pd.read_csv('Dataset/batsman_season_record.csv')

# plt.bar(df['batsman'],df['2015'])
# plt.bar(df['batsman'],df['2017'])
# plt.bar(df['batsman'],df['2016'])


## it will overlap

# Now we will look for side by side bar graph plot 

# -> using width parameter 

np.arange(df.shape[0])

# plt.bar(np.arange(df.shape[0])-0.3,df['2015'],width=0.28,label='2015')
# plt.bar(np.arange(df.shape[0]),df['2016'],width=0.28,label='2016')
# plt.bar(np.arange(df.shape[0])+0.3,df['2017'],width=0.28,label='2017')

# plt.ylabel('Runs')
# plt.legend() 
# plt.xticks(np.arange(df.shape[0]),df['batsman'])   # it will rename the x values on the graph 
# plt.show()


# a problem 

# -> overlaping 

color = ['Green','Red','Blue Blue BlueBlue BlueBlue Blue','Yellow','White']

children = [100,200,280,150,500]

plt.bar(color,children,color='Red')

# here the names are big so this will overlap 
plt.xticks(rotation='vertical')  # it will make the names in vertical form 


## Stacked bar chart 

#%%
# plt.bar(df['batsman'],df['2015'],label='2015')
# plt.bar(df['batsman'],df['2016'],bottom=df['2015'],label='2016')
# plt.bar(df['batsman'],df['2017'],bottom=(df['2015']+df['2016']),label='2017')

# plt.legend()


# Histogram 

# -> Univariate Analysis 
# -> numerical 
# -> Use case - Frequency Count

# hist_data = [10,20,30,40,36,47,38,65,54,34]
# plt.hist(hist_data,bins=[0,10,20,30,40,50])


# vk_hist = pd.read_csv('Dataset/vk.csv')
# vk_hist
# plt.hist(vk_hist[])


# plt.hist(vk_hist['batsman_runs'],bins=[10,20,30,40,50,60,70,80,90,100,110])


## Pi Chart 
# -> Contribution out of 100%(standard scale)

# Univariate/Bivariate Analysis 
# category vs numerical 
# Use case - To find the contribution on a standard scale 

# Simpl data 

contri = pd.Series([20,30,34,46,60],index=['Dev','Devsh','Devendra','Neelam','Papa jI'])

plt.pie(contri,labels=['Dev','Devesh','Devendra','Neelam','Papa jI'],autopct='%0.1f%%',colors=['red','blue','Green','Yellow','orange'],explode=[0.2,0,0,0,0])
# plt.shadow()
# autopct -> For giving the percentage 
## Explode -> To show the graph more visually good
## Shadow -> To show the graph more visually good looking 
plt.style.use('petroff10')


#%%

#::: Changing styles 

plt.style.available

plt.style.use('petroff10')











# %%
