import matplotlib.pyplot as plt
# class uitvoeren:
#     def uitvoer(a,b):
#         plt.plot(a,b)
#         plt.show()
print("tussen welke waarden wil je alles plotten")
getal = int(input())
begingt = getal
laag = getal
rij = []
i = 0
rijx = []
while laag > 4:
    rij.append(laag)
    rijx.append(i)
    i += 1
    if laag % 2 == 0:
        laag = laag/2
    else:
        laag = laag*3+1

laag2 = getal+27
x = []
y = []

while laag2 > 4:
    x.append(laag2)
    y.append(u)
    u += 1
    if laag2 % 2 == 0:
        laag2 = laag/2
    else:
        laag2 = laag*3+1

plt.plot(rijx,rij)
plt.plot(x,y)
plt.show()
#uitvoeren.uitvoer(rijx,rij)

