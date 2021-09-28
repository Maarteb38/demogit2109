import pandas as pd

class kerstkaart:
    naam = "nvt"
    def feestwensen(_self):
        print("vrolijke feestdagen!"+ _self.naam)



# Data inladen
data = pd.read_csv('random123.csv')

#iedereen een vrolijk kersfeest wensen
naamarray = data['name']
for x in range(len(naamarray)):
    q = kerstkaart()
    q.naam=naamarray[x]
    q.feestwensen()
    print(naamarray[x])
    print("de kerstman weet dat je naam dit aantal letters telt:")
    print(len(naamarray[x]))
