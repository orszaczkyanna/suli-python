
#Abszolútérték

absz = int (input("Adj meg egy számot: "))


if absz >= 0:
    print ("A(z)",absz,"szám abszolútértéke: ", absz)
else:
    print ("A(z)",absz,"szám abszolútértéke: ", absz*-1)


if absz >= 0:
    szam = absz
else:
    szam = -absz #-absz = absz * -1

print ("A(z)",absz,"szám abszolút értéke",szam)



#Ugyanez csak bemenetként nem egész szám, hanem valós/lebegőpontos (float) típusú
#2 tizedes hegyre kiíratni

#szam2 = float (input ("Adj meg egy számot: "))



#Háromszög oldalainak hossza
#a) pozitív szám-e, ha nem: hibás bemenet
#b) döntse el, hogy szerkeszthető-e (bármely 2 oldal összege nagyobb mint a 3.)
#c) kerület, terület
#d) döntse-e el, h derékszögű-e

 #változó név betűvel kezdődhet, számmal, betűvel folyt




import math

oa = float (input("Add meg a háromszög 'a'oldalát: "))
ob = float (input("Add meg a háromszög 'c'oldalát: "))
oc = float (input("Add meg a háromszög 'b'oldalát: "))
k = oa+ob+oc
s = k/2
t = math.sqrt(s*(s-oa)*(s-ob)*(s-oc))


if oa<=0 or ob<=0 or oc<=0:
    print("Hibás bemenet")
elif oa+ob <= oc or oa+oc <= ob or oc+ob <= oa:
     print ("A háromszög nem szerkeszthető")
else:
    print ("A háromszög kerülete: {0:.2f}".format(k))
    print ("A háromszög területe: {0:.2f}".format(t))
    if oa**2 + ob**2 == oc**2 or oa**2 + oc**2 == ob**2 or ob**2 + oc**2 == oa**2:
        print ("A hámromszög derékszögű")
    else:
        print ("A háromszög nem derékszögű")


if oa>0 and ob>0 and oc>0:
    if oa+ob > oc and oa+oc > ob and  oc+ob > oa:
        print ("A háromszög kerülete: {0:.2f}".format(k))
        print ("A háromszög területe: {0:.2f}".format(t))
        if oa**2 + ob**2 == oc**2 or oa**2 + oc**2 == ob**2 or ob**2 + oc**2 == oa**2:
            print ("A hámromszög derékszögű")
        else:
            print ("A háromszög nem derékszögű")
    else:
        print ("A háromszög nem szerkeszthető")
else:
    print("Hibás bemenet")    




for i in range (3, 10, -1): #kezdő_érték, vég_érték, lépésköz
    print("palyesz", i)

print("vége a ciklusnak")


#Írassuk ki az első 10 egész számot
for i in range (1, 11):
    print (i, end=" ")




#Írjuk ki egymás alá az első 10 pozitív négyzetszámot
print ("Az első 10 pozitív négyzetszám: ")
for i in range (1,11):
    print (i**2)



#Írjuk egymás alá az első 100 pozitív páros számot
print ("Az első 100 pozitív páros szám: ")
for i in range (0,101):
    print(i*2)



#Első 10 szám csökkenő sorrendben

for i in range (10,0,-1):
    print (i)



#írjuk ki az összes kétjegyű páros számot
for i in range (10, 99, 2):
    print (i)

for i in range (10, 100):
    if i%2==0:
        print (i)



#első 5 természetes szám összege
osszeg = 0
for i in range(1,6):
    osszeg = osszeg + i #osszeg += i
    print ("osszeg= ", osszeg, " i=",i, sep ="")
print ("Az első 5 természetes szám összege: ",osszeg)



#első 5 természetes szám faktoriálisát

fakt = 1
for i in range (1,6):
  fakt = fakt*i
  print ("faktoriális= ", fakt, " i=",i, sep ="")
print ("Az első 5 természetes szám faktoriálisa: ",fakt)




szam = int (input ("Kérek egy számot: "))

fakt = 1
for i in range (1,szam+1):
  fakt = fakt*i
  print ("faktoriális= ", fakt, " i=",i, sep ="")
print ("Az első 5 természetes szám faktoriálisa: ",fakt)



szam = int (input ("Kérek egy számot: "))
fakt = 1
if szam >= 0:
    for i in range (1,szam+1):
        fakt = fakt*i #fakt *= i
    print ("faktoriális= ", fakt, " i=",i, sep ="")
    print ("Az első 5 természetes szám faktoriálisa: ",fakt)
else:
    print ("negatív szám")



szo = input ("Adj meg egy szót: ")
for i in szo:   #a str összes betűjét felveszi
    print (i)



mondat = input ("Adj meg egy mondatot: ")
darab = 0
mgh = 0

for i in mondat:
    if i == " ":
        darab += 1
    elif i == "a" or i == "a" or i == "e" or i == "o" or i == "u":
        mgh += 1

print("A mondat ",darab+1," szóból áll", sep="")
print("A mondatban ",mgh," magánhangzó van", sep="")


"""
#nem jó
csil = "*"
for i in range(5):
    csil = csil+csil
    print (csil)
"""

csil = ""
for i in range(5):
    csil += "* "
    print (csil)
