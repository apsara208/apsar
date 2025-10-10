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
print(my_df)

#add column with assign-creates new df
my_df2=my_df.assign(disabled=[False]*len(my_df))
print(my_df2)