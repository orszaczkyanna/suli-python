
#Kérjük be 3 négyzet oldalának adatát, határozzuk meg, és jelenítsük meg a konzolon a kerületeket



#!FÜGGVÉNY!
#függvény definíciónál
#oldal: formális paraméter
def negyzetkerulet( oldal ):
    K = 4 * oldal
    return K
#függvény paramétere: oldal
#K: visszatérési érték, a hívás helyére kerül

#Ha nincs return, akkor "none" értéket ad, azt jelenti, még nem kapott értéket
#a1,a2,a3 aktuális paraméterek
#*lást: sqrt()
a1 = int (input("1. négyzet oldalának hossza: "))
a2 = int (input("2. négyzet oldalának hossza: "))
a3 = int (input("3. négyzet oldalának hossza: "))

K1 =  negyzetkerulet (a1) #4*a1 
K2 =  negyzetkerulet (a2) #4*a2 !FÜGGVÉNYHÍVÁS!
K3 =  4*a3



print ("1. négyzet kerülete:",K1)
print ("2. négyzet kerülete:",K2)
print ("3. négyzet kerülete:",K3)


#Írj függvényt, ami meghatározza egy négyzet területét

def negyzetterulet (oldal):
    return oldal * oldal

print ("Négyzetek területei sorrendben:",negyzetterulet(a1),negyzetterulet(a2),negyzetterulet(a3))



# Írj függvényt, amely meghatározza egy szám abszolútértékét

def abszolut ( szam ):
    if szam >= 0:
        return szam
    else:
        return -1 * szam

def abszolut2 ( szam ):
    if szam >= 0:
        vissza = szam
    else:
        vissza = -1 * szam
    return vissza 
    #!a return egy tabbal beljebb van mind a def

vmi = int(input("Adj egy számot: "))
print ("Abszolútértéke",abszolut(vmi))
#az abszolut(vmi) KIFEJEZÉS

#d: decimal egész érték
#f: float lebegőpontos (tizedes)
# {X:Y,Zf}
# X: A felsorolásból hanyadik értéket írja ki, 0-val kezdve
# Y: milyen széles mezőn jelenítse meg a számot
# Z: mennyi tizedes jegyre kerekítve jelenjen meg

print ( "{1:d} {0:f}".format(1,3) )
print ( "{1:d} {0:.2f}".format(1,3) )
print ( "{1:d} {0:10.2f}".format(1,3) )
#10 karakternyi helyen jeleníti meg
#{0:10.2f} 1. értéket 10 karakternyi helyen 2 tizedes jegyre




#python kifejezés láncolása

a = 1
b = 2
c = 3


if a < b < c:
    pass

#máshol:
if a < b and b < c:
    pass



# Írj ELJÁRÁST, amely egy dátumot vár paraméterül
# "éééé.hh.nn" formában
# a dátumot jelenítse meg
# "éééé év hh. hónap nn.nap"
# pl.: "2021.11.09" -> "2021. év 11. hó 09. nap"

#!ELJÁRÁS
def kiirdatum ( datum ):
    darabolt = datum.split(".")
    print (darabolt[0],". év ", darabolt[1],". hónap ",darabolt[2],". nap", sep="")

kiirdatum ("2021.11.09")
kiirdatum (input("Adj meg egy dátumot: "))


#függvény: értéket határoz meg
#eljárás: utasításokat hajt végre egymás után, amiben print van az eljárás

#függvénynek van visszatérési értéke, eljárásnak nincs



lista1 = ['alma','körte','szilva']
lista2 = [1,2,3,4]
# '-es és "-es ugyanaz

for i in lista1:
    print (i)
for i in lista2:
    print (i)


def kiirlista (lista):
    for i in lista:
        print (i, end=" ")
    print("")

kiirlista( lista1 )
kiirlista( lista2 )

#Debugban Step into F11, belemegy az alprogramba
#F10-zel nem megy a függvénybe


#HF: Írj függvényt, amely meghatározza egy téglalap kerületét
#valamint egy függvényt, amely meghatározza a téglalap területét


# Írj függvényt, amely meghatározza egy pozitív egész szám osztóinak számát
# olvass be 5 számot, és írasd ki ezen számok osztóinak számát
# ".. . osztóinak száma ..." formában
# pl.: 6 osztóinak száma 4

def oszto (szam):
    darab = 0
    for i in range( 1 , szam+1 ):
        if szam % i == 0:
            darab += 1
    return darab

print ("Adj meg 5 számot")
for i in range (5):
    bekert = int ( input("Adj meg egy számot: ") )
    print (bekert,"osztóinak száma",oszto(bekert))




"""
#nem működik
szamlista = []

for i in range (5):
    szamlista[i] = input("Adj meg egy számot: ")

for i in range (5):
    print (szamlista[i],"osztóinak száma",oszto(szamlista[i]))

"""


# Írj függvényt, amely meghatározza egy szám faktoriálisát

def fakt (szam):
    f = 1
    for i in range (1, szam+1):
        f = f * i
    return f

print  ( fakt(5) )



# Írj függvényt, amely meghatározza az n alatt a k értéket
# (n alatt k) = n! / k!*(n-k)!

def n_k (n , k):
    nfakt = fakt ( n )
    kfakt = fakt (k)
    nminuszkfakt = fakt (n-k)
    return nfakt / (kfakt*nminuszkfakt)
    return fakt ( n ) / (fakt (k)*fakt (n-k))

#return után többi utasítás nem fut le

print (n_k (5,2))

#gyakorlás pl. egyenlet gyökei etc.
# első n természetes szám összege

import math
math.factorial()
math.gcd() #legnagyobb közös osztó
#legkisebb közös többszörös

