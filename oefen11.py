import pandas as pd

class kerstkaart:
    naam = "nvt"
    def feestwensen(self):
        print("vrolijk feestdagen!")



# Data inladen
data = pd.read_csv('random123.csv')

#iedereen een vrolijk kersfeest wensen
naamarray = data['name']
for x in range(len(naamarray)):
    kerstkaart.feestwensen(x)
    print(naamarray[x])
    print("de kerstman weet dat je naam dit aantal letters telt:")
    print(len(naamarray[x]))
