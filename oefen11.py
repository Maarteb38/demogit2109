import pandas as pd

# Data Inladen
data = pd.read_csv('random123.csv')
print(data.head(n=10))

# Data Schoonmaken
data.columns = data.columns.str.upper().str.replace('_', '')
print(data.head())

data = data.set_index('name')
data=data.drop(['#'], axis=1)
data=data.drop(['generation'], axis=1)
data=data.drop(['legendary'], axis=1)
data['TYPE 2'].fillna(data['TYPE 1'], inplace=True)
print(data.head(10))