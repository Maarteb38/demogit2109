import array

import pandas as pd

class Kerstkaart:
    naam = "nvt"
    def feestwensen(_self):
        print("vrolijke feestdagen! "+ _self.naam)




# Data inladen
data = pd.read_csv('random123.csv')

#iedereen een vrolijk kersfeest wensen
naamarray = data['name']
for x in range(len(naamarray)):
    q = Kerstkaart()
    q.naam=naamarray[x]
    mandje = [1 , 'piet']
    mandje.append(q.feestwensen())


print(mandje)
