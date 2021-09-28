import pandas as pd

# Data inladen 
data = pd.read_csv('random123.csv')
print(data.head(n=10))

# Data schoonmaken
data.columns = data.columns.str.upper().str.replace('_', '')
print(data.head())

data = data.set_index('NAME')
data=data.drop(['#'], axis=1)
data=data.drop(['GENERATION'], axis=1)
data=data.drop(['LEGENDARY'], axis=1)
data['TYPE 2'].fillna(data['TYPE 1'], inplace=True)
print(data.head(10))