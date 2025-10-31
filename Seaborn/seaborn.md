## Data Vizualization with [Seaborn]
-> It is an adavance library which is used for the datavizualization 
-> It provides more graph than traditional library like matplotlin
-> This is most popular to use in the data vizualization process
-> 

## It has two types of of functions 

[1]. Figure Level : These are like higher level function which   
     includes many axis level functions or graphs like scatter plot
[2]. Axis level: These are the kind of graphs which are used in axis 
     level data vizualization


## Thre are five main categories of the plots  

 1. Relational plots, Purpose: Show relationships between two or more
    variables. [linepplot()/scatterplot()]  relplot()

 2. Distribution, Purpose: Display how data points of a variable are 
    distributed.  [histplot()/kdeplot()/ecdplot]    

 3. Matrix plot, Purpose: Visualize relationships between a 
    categorical variable and another [boxplot()/barplot()/stripplot()]

 4. Regration plot, Purpose: Show the relationship between two 
    variables with a fitted regression model [regplot()/implot()]          
 
 5. Matrix plots, Purpose: Visualize entire matrices, such as 
    correlations or heatmaps.[heatmap()/clustermap()]

 6. Multi-Plot Grids, Purpose: Visualize relationships or 
    distributions for multiple variables at once.[pairplot()/jointplot()]



# Category      |  Example Functions                      |  Typical Questions Answered                         
----------------+-----------------------------------------+-----------------------------------------------------
Relational      |  scatterplot, lineplot, relplot         |  How do variables relate?                           
Distribution    |  histplot, kdeplot, displot             |  How is a variable distributed?                     
Categorical     |  boxplot, barplot, violinplot, catplot  |  How does a numeric value differ across categories? 
Regression      |  regplot, lmplot                        |  Is there a trend or relationship (with regression)?
Matrix          |  heatmap, clustermap                    |  What are the relationships in a matrix?            
Pairwise/Joint  |  pairplot, jointplot                    |  How do all variables relate or distribute?         


# Facet Plot: 

[1]. To compare trends, distributions, or 
     relationships across groups

[2]. When you want to visualize multiple 
     subsets of data side-by-side

[3]. For exploratory data analysis, 
     especially with complex or multi-dimensional datasets


# Categorical plot 