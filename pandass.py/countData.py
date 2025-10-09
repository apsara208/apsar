import pandas as pd
import numpy as np
from numpy.random import randn
my_data=randn(4,3)
my_row=['a','b','c','d']
my_cols=["mon","tues","wed"]
my_df=pd.DataFrame(my_data,my_row,my_cols)
print(my_df)
#count distinct values: Descending
print(my_df["mon"].value_counts())
print(my_df["mon"].value_counts(ascending=True))
print(my_df["mon"].value_counts(dropna=False)) #NaN value : null vLues

#get relative frequency -percentage
print(my_df["mon"].value_counts(normalize=True))
#get specific item count
#print(my_df["mon"].value_counts()[0.591120])
#cout unique values-size
#print(my_df.groupby("color").count())

#get a count of all columns across all  columns
print(my_df.apply(pd.value_counts))