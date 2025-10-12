import pandas as pd
import numpy as np
my_df=pd.read_csv("people_short.csv")
#print(my_df)

#add col from list -small dataset
salary=[5000,3000,2000,4000,1000]
my_df["salary"]=salary
#print(my_df)

#add default value
my_df["alive/dead"]=["alive"]*len(my_df)
#print(my_df)

my_df["1st year"]=[np.nan]*len(my_df)
#print(my_df)

#add coolumn with .insert()
my_df.insert(1,"straight",[True]*len(my_df),True)
#print(my_df)

#add column with assign-creates new df
my_df2=my_df.assign(disabled=[False]*len(my_df))
#print(my_df2)

#axis is the row ur column name whole sequence: row names is axis 0 and column names is axis 1
#remove col
my_df.drop("straight",axis=1,inplace=True)
#print(my_df)

#remove row : degfault axis is 0
my_df.drop(3,inplace=True)
#print(my_df)

#grab row method 1 location
a=my_df.loc[1]
#print(a)

#grab row method 2: index location
#index location is index number
b=my_df.iloc[3]
#print(b)

#specific point(rows and cols)
#my_df.loc["row","column"]
c=my_df.loc[1,"First Name"]
#print(c)

#subsets
#my_df[["row","row"],["column","column"]]
d=my_df.loc[[1,2],["Last Name","First Name"]]#order here matters not of the data frame 
#last name will be given before first name , contrasting the data
print(my_df)