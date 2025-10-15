import pandas as pd

#cleaning null values
'''
df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())
'''
#cleaning values of a specific column
#df.dropna(subset=['Date'], inplace = True)

#filling null values
#df.fillna(130, inplace = True)

#filling null values of a specific column
#f.fillna({"Calories": 130}, inplace=True)

#cleaning wrong format 
#example wromg format
'''
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())
'''

#replacing values 
#df.loc[7, 'Duration'] = 45
#replaced value at loaction 7 of column "Duration"


#removing duplicates
#print(df.duplicated())
#Returns True for every row that is a duplicate, otherwise False:

#df.drop_duplicates(inplace = True)