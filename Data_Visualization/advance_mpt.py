#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


iris = pd.read_csv('dataset_1/iris.csv')


# plotting the scatter plot 
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'])
# plt.xlabel('SepalLengthCm')
# plt.ylabel('PetalLengthCm')
# plt.show()

# -> providing the number to the species name 

# sampling the random data 
# iris.sample(5)

# providing the numbers to the diffrent species 

iris['Species'] = iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})

# iris.sample()

# -> Here a hidden parameter c is used to give the points --> It also provide different class and colors 
plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='jet')
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')

# it will give the size of the plot (expand or reduce the size)

plt.figure(figsize=(20,11))

# -> CMap:: It gives the color coding of the data 
# -> Colorbar -> It gives the colrbar of values (low -> high )
plt.colorbar()  


#%%
##:::::::: Plot Size 

batters = pd.read_csv('dataset_1/batter.csv')

sample_df = batters.head(100).sample(25)


""""  :::::::::::: Annotation ::::::::::::::: """
# -> It is used to provide the names of the data points 

plt.figure(figsize=(20,12))
plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs'])

# here s is used to show the size of the bubbles 

# x = [1,2,3,4]
# y = [5,6,7,9]
# plt.scatter(x,y)
# # uisng text 
# plt.text(1,5,"Point 1")
# plt.text(2,6,"Point 2")
# plt.text(3,7,"Point 3")
# plt.text(4,9,"Point 4",fontdict={'size':10,"color":'red'})


# -> Using loops 
for i in range(sample_df.shape[0]):
     plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i])

### ::::::::::;Horizontal and Vericle Lines 

# -> Drawing a horizontal or verticle line 

# Players having the strike rate is greater than 150
plt.axhline(150,color='green')

# having the average is greater than 30 

plt.axvline(30,color='red')

plt.show()



""":::::::::::::::::::::::: Suplots::::::::::::::::::"""

#%%


# -> Three are multiple ways to draw plots in mpl

# -> Here is the second method of drawing the graphs 


# fig,ax = plt.subplots(figsize=(15,8))

# ax.scatter(batters['avg'],batters['strike_rate'])
# ax.set_title('Virat vs Rohit')
# ax.set_ylabel('strike_rate')
# ax.set_xlabel('avg')

# Subplot 

fig, ax = plt.subplots(nrows=2,ncols=1,figsize=(16,12),sharex=True)

ax[0].scatter(batters['avg'],batters['strike_rate'],color='green')
ax[1].scatter(batters['avg'],batters['runs'])


ax[0].set_title('Avg vs Strike_rate')
ax[1].set_title('Avg vs Runs')

ax[0].set_ylabel('Average')
ax[0].set_xlabel('Strike_Rate')


## Now plotting 4x4 

#%%
fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(12,12))

ax[0,0].scatter(batters['avg'],batters['strike_rate'],color='green')
ax[0,0].set_xlabel('Average')
ax[0,0].set_ylabel('Strike-Rate')
ax[0,1].scatter(batters['avg'],batters['runs'],color='Red')
ax[0,1].set_xlabel('Average')
ax[0,1].set_ylabel('Runs')
ax[1,0].hist(batters['avg'],color='orange')
ax[1,1].hist(batters['runs'])



"""::::::::::::::: 3D Scatter Plot Graphs ::::::::::::"""
 
 #%%
 
# fig = plt.figure(figsize=(10,10))

# ax = plt.subplot(projection='3d')
 
# ax.scatter3D(batters['avg'],batters['strike_rate'],batters['runs'])
 
# ax.set_xlabel('Average')
# ax.set_ylabel('Strike-Rate')
# ax.set_zlabel('Runs')


### :::::::: 3D Line Plot 

x = [0,1,7]
y = [1,8,12]
z = [3,5,15]

fig = plt.figure()
ax  = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,120,130],color='red')

ax.plot3D(x,y,z)



""" ::::::::: 3D Surface Plots :::::::"""

#%%
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

# plotting a mesgrid 
xx, yy = np.meshgrid(x,y)

xx.shape

z = xx**2 + yy**2
# z.shape

# z = np.sin(xx)+np.cos(yy)
fig = plt.figure(figsize=(10,10))

ax = plt.subplot(projection='3d')

# circle = ax.plot_surface(xx,yy,z,cmap='viridis')

# fig.colorbar(circle)



""":::::::::::::::::::::: Contour Graph ::::::::::::::::::::"""

#%%
# -> this converts the 3d into 2d 

fig = plt.figure(figsize=(12,8))

ax = plt.subplot(projection='3d')


circle = ax.contourf(xx,yy,z,cmap='viridis')

plt.show()




""":::::::::::: Heat Map :::::::::::::::"""

#%%

# making a pivot table of the data of ipl per ball 
delivery = pd.read_csv('dataset_1/IPL_Ball_by_Ball_2008_2022.csv')

delivery.head()

# dataframe filtering
df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run']==6)]

# making a grid to make a heatmap
grid = df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')

plt.figure(figsize=(12,8))

# imshow() is used to show the heatmap
plt.imshow(grid)
plt.yticks(delivery['overs'].unique(),list(range(1,21)))
plt.xticks(np.arange(0,6),list(range(1,7)))
plt.colorbar()




#%%
""" ::::::::::::::: Pandas Plot( ) ::::::::::::::::::    """


# ps = pd.Series([1,2,3,4,5])

# ps.plot(kind='pie')


import seaborn as sns 

tips = sns.load_dataset('tips')

tips.head()


## scatter Plot -> labesl -> markers -> figsize -> color -> cmap


# tips.plot(kind='scatter',x ='total_bill',y='tip',title='cost Analysis',marker='*',c='sex',colormap='viridis')


## :::::: 2d plot 

stocks = pd.read_csv('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv')

# stocks.head()

# line plot 

# stocks['MSFT'].plot(kind='line')

# stocks.plot(kind='line',x='Date')

# only two 

# stocks[['FB','MSFT']].plot(kind='line')


# Bar chart  single -> Horizontal -> muliple 

# using tips
# tips.plot(kind='bar',x='sex',y='total_bill')


# using group by  --> Because group by used to give groups 


tips.groupby('sex')['total_bill'].mean().plot(kind='bar')


# Pandas can handle bar chart very efficiently 

# It can help in bar chart, 


## histogram using pandas plot function 

stocks[['FB','MSFT']].plot(kind='hist',bins=40)



### pie chart using pandas 

#%%
df = pd.DataFrame(
    {
        'batsman':['Dhawan','Rohit','Kohli','SKY','Pandya','Pant'],
        'match1':[120,90,35,45,12,10],
        'match2':[0,1,123,130,34,45],
        'match3':[50,24,145,45,10,90]
    }
)

df['match1'].plot(kind='pie',labels=df['batsman'].values,autopct="%0.01f%%")



## pie subplot 

df[['match1','match2','match3']].plot(kind='pie',subplots=True)

 























# %%
