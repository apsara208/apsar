#The corr() method calculates the relationship between each column in your data set.
import numpy as n
import pandas as pd
my_df=pd.read_csv("sales.csv")
numeric_df=my_df.select_dtypes(include="number")
print(numeric_df.corr())