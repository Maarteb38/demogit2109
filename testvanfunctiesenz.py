print("Hoi zeg me eens hoeveel getallen je wilt gaan invoeren?")
AantalG = int(input())

print("Met welk getal wil je gaan optellen?")
Optel = int(input())
Print("Maar wat ")
print("dus je wilt", AantalG, "gaan printen en met", Optel, "gaan optellen")
PArray = []
SomArray = []
SpiegelArray = []
print("en nu mag je het volgende aantal gaan invoeren")

print(AantalG)
for i in range(AantalG):
    PArray.append(int(input()))
for i in range(AantalG):
    g = PArray[i] + Optel
    SomArray.append(g)
print(PArray)
print(SomArray)
print("wil je nog gaan spiegelen dan? J is Ja, iets anders is nee")
keuze = input()
if keuze == "J":
    SomArray.reverse()
    print(SomArray)