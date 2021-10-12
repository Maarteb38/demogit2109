class Meegeven:
    goed = []
    def Functie(goed, a):
        aantalx = goed.count(a)
        print(aantalx)

print("hoelang is het array?")
length = int(input())
print("getallen array van", length,"lang")
getar = []
for x in range(length):
    getar.append(int(input()))
print("wat is het zoekgetal?")
getget = int(input())

Meegeven.Functie(getar,getget)