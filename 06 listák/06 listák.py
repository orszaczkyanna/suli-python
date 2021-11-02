lista = [3,6,25,8,25,22,12]

#lista legnagyobb eleme

legnagyobb = lista[0] 
for i in lista:
    if i > legnagyobb:
        legnagyobb = i

print ("A lista legnagyobb eleme: ", legnagyobb)

# lista legnagyobb elemének a helye

maxindex = 0

for i in range (0, len(lista)):
    if lista [i] > lista [maxindex]: # >= ha a legutolsó kell a legnagyobbnak
        maxindex = i

print ("A lista legnagyobb elemének (első)helye:", maxindex)

#Ha az első a legnagyobbak közül, akkor > *az első, amit megtalál az marad
#ha a legutolsó >= *ha egyenlő lesz, akkor is felülírja
#vagy
#fordítva járjuk be a listát (csökkenő sorrendben)


maxindex = len(lista) - 1
#utolsó elem mindig len(lista)-1
for i in range (len(lista)-1,-1,-1):
    if lista [i] > lista [maxindex]:
        maxindex = i

print ("A lista legnagyobb elemének (utolsó)helye:", maxindex)

#HF: megkeresni a legkisebb elemet és annak a helyét

#Új elem hozzáadása listához
lista.append(36)
print (lista)

#új elem megadott indexszámhoz
lista.insert(2, 999)
#kettes indexre 999. A többit arrébb tolja


#az elemet (25) az első előfordulási helyéről törli
#egy adott értékű elem törlése, ez csak az első előfordulást törli
lista.remove (25)


#lista minden adott értékű elem (25) törlése
while 25 in lista:
    lista.remove(25)


# lista fordítottja
lista.reverse() # helyben megfordítja (mint utasítást adom ki?)
print ("lista fordítottja",lista)
lista.reverse() #visszafordít
print ("lista dupla fordítottja",lista)


lista.sort() #növekvő sorrendbe rendezi
print ("Rendezett lista:",lista)

#csökkenő sorrendbe:
lista.sort()
lista.reverse()
#vagy
lista.sort(reverse=True)

#stringeknél abc sorrendben * ékezeteseket különleges karakternek veszi



#Írj egy programot, amely bekéri 5 család jövedelmét és meghatározza a legnagyobb és legkisebb jövedelmet
#Határozza meg az öt család összjövedelmét és átlag jövedelmét
#Hanyadik családnak van a legnagyobb jövedelme 


from typing import ValuesView


jovedelmek = []


for i in range(5):
    print("Kérem a(z) ",i+1,".család jövedelmét: ", sep ="", end="")
    be = int(input())
    jovedelmek.append(be)

print("A felhasználó által megadott adatok:",jovedelmek)

legnagyobb = jovedelmek[0]
legkisebb = jovedelmek[0]

for i in jovedelmek:
    if i > legnagyobb:
        legnagyobb = i
    if i < legkisebb:
        legkisebb = i
        
print("A legnagyobb érték:",legnagyobb)
print("A legkisebb érték:",legkisebb)

ossz = 0
for i in jovedelmek:
    ossz += i
atlag = ossz/len(jovedelmek)
#atlag1 = ossz/5

print ("Összjövedelem:",ossz)
print("Átlagos bevétel:",atlag)


maxindex = 0
for i in range(len(jovedelmek)):
    if jovedelmek[maxindex] < jovedelmek[i]: #!!! relációs jel iránya
        maxindex = i
print("A legnagyobb jövedelem a(z) ",maxindex+1,". családnak van", sep="")





# Kérd be 5 hívás adatát pp:mm formában
# írd ki, melyik volt a leghosszabb hívás
# ha nem jó formában adta meg a bemenetet, akkor írjon hibaüzenetet és fejezze be a program futását

print ("Add meg 5 hívás hosszát 'pp:mm' formában")

hivasok = []

for i in range(5):
    print("Kérem a(z) ",i+1,".hívás hosszát: ", sep ="", end="")
    be = input()

    if len(be) != 5:
        print("Hibás híváshossz")
        break
    if be[2] != ":":
        print("Hibás híváshossz")
        break

    seged = be.split(":") #két elemű lista lesz

    # lexikografikus (abc sorrendben) értelmezi a stringet
    if seged[0] < "00" or seged[0] > "59" or seged[1] < "00" or seged[1] > "59": #idézőjelbe kell tenni, nem számokként fogja értelmezni, hanem string abc sorrend, intervallumba esik-e
        print("Rossz híváshossz")
        break

    hivasok.append(be)


if len(hivasok) != 0:
    print( hivasok )
    maxhossz = hivasok[0]

    for hivas in hivasok:
        if hivas > maxhossz:
            maxhossz = hivas
    print("A leghosszabb hívás:",maxhossz)
else:
    print("Nem volt megadva érvényes hossz")


#Olvass be 6 szót, majd írd ki a leghosszabbat és a legrövidebbet

print("Adj meg 6 szót")

szavak = []
for i in range(6):
    be = input()
    szavak.append(be)

print("A beírt szavak:",szavak)
leghosszabbszo = szavak[0]
legrovidebbszo = szavak[0]



for szo in szavak:
    if len(szo) > len(leghosszabbszo):
        leghosszabbszo = szo
    if len(szo) < len(legrovidebbszo):
        legrovidebbszo = szo

print("A leghosszabb szó:",leghosszabbszo)
print("A legrövidebb szó:",legrovidebbszo)




#Kérj be szavakat a 'stop' szó beírásáig, majd írd ki mennyi szót írtál be
#Egészítsd ki a programot, hogy a STOP sTop Stop etc. változatra is állítsa meg

print("Írj be a szavakat, ha végeztél, írd be, hogy 'stop'")

darab = 0
be = input()

while be.lower() != "stop":
    darab += 1
    be = input()

print ("Összesen",darab,"szót írtál be")



# gondoltam egy számra 1 és 100 között
# a program kérjen tippeket a gondolt számra, ha talált, írja ki, hogy eltaláltad
# ha nem, akkor írja ki, hogy a gondolt szám kisebb vagy nagyobb a tippnél
#A felhasználó max 12-szer próbálkozhat


#gondolt = 68

import random
gondolt = random.randint(1,100)
probalkozas = 12
print("Gondoltam egy számra 1 és 100 között, maximum 13-szor tippelhetsz")

while probalkozas > 0:
    print ("Kérek egy tippet: ", end="")
    tipp = int(input())

    if tipp == gondolt:
        print ("Eltaláltad")
        break
    elif gondolt > tipp:
        print ("A gondolt szám nagyobb, mint a tipped, még",probalkozas,"próbálkozásod van")    
    else:
        print ("A gondolt szám kisebb, mint a tipped, még",probalkozas,"próbálkozásod van")

    probalkozas -= 1
    if tipp > 100 or tipp < 1:
        probalkozas += 1
        print("Csak 1 és 100 közé eső számokat adj meg")

if probalkozas == 0:
    print("Vesztettél, a(z)",gondolt,"számra gondoltam")