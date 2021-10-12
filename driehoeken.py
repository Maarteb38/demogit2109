import decimal

import matplotlib.pyplot as plt
import math
class checken:
    def tekenen(a,b,c):
        plt.title(a)
        plt.plot(b, c)
        plt.show()

print("noem 3 x 2 punten (min 0  max 10)")
rij = []
for i in range (6):
    print(i)
    punt = int(input())
    if 0 < punt < 10:
        rij.append(punt)
    else:
        print("niet zo he makker")
        i = 0
lengteA = math.sqrt(abs(rij[0]^2+rij[2]^2+abs(rij[1]^2+rij[3]^2)))
lengteB = math.sqrt(abs(rij[2]^2+rij[4]^2+abs(rij[3]^2+rij[5]^2)))

uitslag = round(lengteA,3), round(lengteB,3)
x = [rij[0],rij[2],rij[4],rij[0]]
y = [rij[1],rij[3],rij[5],rij[1]]
checken.tekenen(uitslag,x,y)