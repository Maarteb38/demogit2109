class Meegeven:
    goed = []
    def Functie(goed, a):
        aantalx = goed.count(a)
        print(aantalx)

print("getallen array 3")
getar = []
for x in range(3):
    getar.append(int(input()))
print("wat is het zoekgetal?")
getget = int(input())

Meegeven.Functie(getar,getget)