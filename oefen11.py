import pandas as pd

# Data inladen
data = pd.read_csv('random123.csv')

print("wat wil je weten naam=N of generation=C?")
vraag = str(input())
Name = "N" or "n"
Cate = "C" or "c"

if vraag==Name:
    print(data["name"])
if vraag==Cate:
    print(data["generation"])
# Data schoonmaken
data.columns = data.columns.str.upper().str.replace('_', '')

