import pandas as pd
import numpy as np
from numpy.random import randn
#dataframes
my_data=randn(4,3) #rows,columns
my_rows=["a","b","c","d"]
my_cols=["monday","tuesday","wednesday"]
#create dataframe
my_df=pd.DataFrame(my_data,my_rows,my_cols)
print(my_df)

#import csv file
#my_df2=pd.read_csv("files.csv")

#pull out rows
#my_df2.loc[0] #first row(horizontal)
 
my_d=pd.read_csv

 #add new column
