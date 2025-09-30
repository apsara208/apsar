import pandas as pd
#jupyter notebook
#series
my_series=[5,9,12,27]
my_var=pd.Series(my_series)
print(my_var)
'''0     5
1     9
2    12
3    27
dtype: int64k'''
my_var2=pd.Series(my_series,["a","b","c","x"])
print(my_var2)
'''a     5
b     9
c    12
x    27
dtype: int64'''
print(my_var2["b"])
"9"

#dictionary
cars={"tesla":12,"mercedes":44,"BMW":4}
my_var3=pd.Series(cars)
print(my_var3)