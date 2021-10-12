for i in range (1,6):
    kiiratni = str(i) + ". szám:"
    szam = int(input(kiiratni))

for i in range (1,6):
    kiiratni = str(i) + ". szám:"
    szam = int(input(i,". szám: "))





print ("Hello Word")

a = 5
b = 6
c = 7
x = -2
y = 3.8
s = "almafa"
k = True



fakt = 1
for i in range (1,5):
    fakt *= i
print ("5 faktoriálisa: ", fakt)
print ("Vége a programnak")



szoveg = "A béka brekeg és fázik."

for i in szoveg:
    print (i)




#Olvass be számokat addig, amíg a felhasználó nullát nem ír be
#Nulla után írd ki, hogy kész


szam = int(input ("Írj be egy számot: "))
while szam != 0:
    szam = int(input ("Írj be egy számot: "))
print ("Kész")

#Ha  feltétel igaz, végrehajtja
#ADDIG hajtja végre újra, amíg a feltétel IGAZ
#Ha a feltétel hamishoz ér, akkor következőre ugrik, kilép a ciklusból

#Végtelen ciklus lesz, ha sosem vesz fel hamis értéket
#konzolban CTRL + C megállítja a program futását
#Ha egyszer sem fut le: üres ciklus




#break: leállítja a ciklus futását
szam = int (input("Kérek egy számot: "))
while True:
    if szam == 0:
        break  #megállítj a ciklust

print("Kész")


#Kérjünk be egy számot, döntsük el, hogy prím-e

szam = int (input ("Adj meg egy számot:"))
prim = True

for i in range(2,szam):
    if szam % i == 0:
        prim = False
        print ("Találtam egy osztót")
        break

if szam <=1:
    prim = False


if prim == True:
    print ("A szám prím")
else:
    print ("A szám nem prím")

# range (kezdő érték, végérték)
# Az intervallumban kezdőértéknek kisebbnek kell lennie a végértéknél 
# Ha csökkenő sorrendben generáljuk, akkor fordítva (pl. 10,1,-1) (*Az 1 már nincs benne)
# Ha a 2 egyenlő, nem csinál semmit. Nem jelez hibát, nem számít hibának


#program leállítása bárhol
#import sys
#sys.exit()  #gyorsabb

#import os
#os.abort()



# bekér 0-ig
# majd kiírja az összeget

szam = int (input("Kérek egy számot: "))
osszeg = 0

while szam != 0:
    osszeg += szam
    szam = int (input("Kérek egy számot: "))

print ("A beírt számok összege", osszeg)



# írjuk ki az egyjegyű pozitív egész számokat

#for i in range (1,10):
#    print(i)

szam = 1
while szam < 10:
    print (szam)
    szam += 1


# ----- LISTA ----
lista = [11,22,33, "string", True] #A [] között vesszővel elválasztva sorolom fel a lista elemeit

lista.append("másik elem") #listához új elemet így adunk (*"lista" nevű listához)

#Lista kiíratása for ciklussal:
for i in lista: #az 'i' sorban felveszi a lista elemeit
    print (i)

print(lista[3]) # A 'lista' hármas indexű (azaz 4.) elemét írja ki (*0-tól indulnak az indexek)

#Lista kiíratása elemenként:
print ( lista[0] )
print ( lista[1] )
print ( lista[2] )
print ( lista[3] )



# 0ig kér számot, tárolja listában
# határozzuk meg
# hány páros, hány páratlan, hány pozitív
# bekért számok átlaga



szam = int(input ("Kérek egy számot: "))
lista = [] # lista deklarálása

paros = 0
paratlan = 0
pozitiv = 0
osszeg = 0

while szam != 0:
    lista.append (szam)
    szam = int(input ("Kérek egy számot: "))

for i in lista:
    if i >= 0:
        pozitiv += 1
    if i%2 == 0:
        paros += 1
    else:
        paratlan += 1

for i in lista:
    osszeg += i
darab = (len (lista) ) #lista hány elemet tartalmaz ((length, lista méretének lekérdezése (stringre is működik)
#"kutya" szó len --> ahán betűből áll --> 5
print(paros," db páros, és",paratlan,"db páratlan számot adtál meg")
print(pozitiv,"db pozitív számot adtál meg")

if darab > 0:
    print("A bekért számok átlaga: ",osszeg/darab)
else:
    print("0 elemnek nincs átlaga")



# Határozza meg az első n természetes szám összegét
# 1 + 2 + ... + (n-1) + n
#2 max 3 sor
#5 -> 15

n = int (input ("Adj meg egy számot: "))
print ("Az első",n,"természetes szám összege",n*(n+1)/2)




import math
print ("szám:", math.factorial(szam))




szam = int (input ("Adj meg egy számot: "))
osszeg = 0
for i in range (0,szam):
    osszeg += szam
print ("Összeg: ",osszeg)

