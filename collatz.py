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
x = [1,2,3,4,5]
y = [4,5,6,7,8]

plt.plot(rijx,rij)
plt.plot(x,y)
plt.show()
#uitvoeren.uitvoer(rijx,rij)

