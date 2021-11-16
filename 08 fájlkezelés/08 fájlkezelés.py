# Futtatás előtt a terminálban a fájl helyére kell navigálni!

# 1. Írj függvényt, amely meghatározza egy pozitív egész szám osztóinak számát
# Olvass be 5 pozitív egész számot és határozd meg az osztóinak számát, írasd ki "...osztóinak száma ..." formában
# írd ki azt a számot, amelyiknek a legtöbb osztója van
# ha több számnak is ugyanannyi osztója van, mint a legtöbb, akkor a többit is írja ki


def osztok_szama (szam):
    #szam = 1
    osztok = 0
    for i in range (1,szam+1):
        if szam % i == 0:
            osztok += 1
    return osztok

szamok = []
for i in range (5):
    be = int(input("Adj meg egy pozitív egész számot: "))
    szamok.append(be)

legnagyobbosztok = 0
for i in szamok:
    if osztok_szama(i) > legnagyobbosztok:
        legnagyobbosztok = osztok_szama(i)

print ("A legnagyobb osztók száma:",legnagyobbosztok)

for i in szamok:
    if osztok_szama(i) == legnagyobbosztok:
        print(i,"osztóinak száma:",legnagyobbosztok)





# FÁJLKEZELÉS

#Írd ki a neved a nevem.txt fájlba

# open függvény paraméterei:
# 1. paraméter: egy fájlnév
# 2. paraméter: megnyitási mód:
#   w: megnyitás írásra (ha már létezik a fájl, akkor felülírja) (write)
#   r: megnyitás olvasásra (read)
#   a: megnyitás hozzáfűzésre (append)
# 3. paraméter: fájl kódolás beállítása

# ekkor a nevem.txt fájlt a python hozzárendeli az f változóhoz
# az f változó segítségével tudjuk a fizikai fájlt olvasni/írni

#f = open("nevem.txt","w", encoding = "utf8")
#f = open("h:\\pythonfeladat\\nevem.txt","w", encoding = "utf8")

f = open("nevem.txt","w", encoding = "utf8")
f.write( "Jane Doe\n" ) #fájlba írás
f.write("másik sor\n")  #\n enter
f.close() # fájl lezárása

f = open("nevem.txt","a", encoding = "utf8")
f.write( "Append, hozzáfűzünk\n" ) #fájlba írás
#!!! f = open, (..nem f pont open, hanem = egyenlő!!)
f.close()


# Olvass be a billentyűzetről egy mondatot (szöveget enterig)
# majd írd ki a text.txt fájlba a beolvasott szöveget szóközök nélkül
# pl.: Bemenet: A béka..

be = input("Adj meg egy mondatot: ")
szokozmentes = be.replace(" ", "")
print(szokozmentes)


f = open("text.txt","w",encoding="utf8") #"a"-val is létrehozza, ha még nem létezik a fájl
f.write(szokozmentes)
f.write(" \n VAGY \n ")

darabolt = be.split(" ")
for i in darabolt:
    f.write(i)

f.close() #!!zárójelek





# Írj programot, amely bekér két egyész számot, majd az eredmény.txt fájlba kiírj a két szám összeg, különbségét, szorzatát a következő formátumban:
# ( x + y = eredmény )
# ( 5 + 6 = 11 )
# ( 5 - 6 = -11 )
# ( 5 * 6 = 30 )

a = int(input("Add meg az első számot: "))
b = int(input("Add meg a másik számot: "))

# osszeg = a + b
# kulonbseg = a - b
# szorzat = a * b

osszeg = str(a + b)
kulonbseg = str(a - b)
szorzat = str(a * b)
a = str(a)
b = str(b)

f = open("eredmény.txt","w", encoding="utf8")
f.write( "( " + a + " + " + b + " = " + osszeg + " )\n" ) 
#plusszal fűzünk össze write-ban (mert a write egy darab stringet tud),, + nem csinál szóközöket mint a ,

f.write( "( " + a + " - " + b + " = " + kulonbseg + " )\n" ) 
f.write( "( " + a + " * " + b + " = " + szorzat + " )\n" ) 


f.write("\n=====\n\n")

#másik stringgé alakítási mód:
a = int(a)
b = int(b)

f.write( "( " + str(a) + " - " + str(b) + " = " + kulonbseg + " )\n" ) 
# ! ezzel nem írom felül a változót, mint a b = str(b)-vel (új változóba is tehetem, inkább abba tegyem)




f = open("nevek.txt","r", encoding="utf8")

nevek = f.read() #egy nagy stringként olvassa be, amiben vannak enterek (\) is
f.close

nevlista = nevek.split("\n")


#Írjuk ki a neveket, és mellé, hogy milyen hosszúak
for nev in nevlista:
    print (nev,":", len(nev))


# keressük meg a leghosszabb nevű embert

leghosszabb = nevlista[0] #ne hasonlítsunk össze olyan elemmel, ami nincs a listában
for nev in nevlista:
    if len(nev) > len(leghosszabb):
        leghosszabb = nev

print("A leghosszabb név: ",leghosszabb)

# hanyadik  a névsorban a leghosszabb nevű ember

index = 0

for i in range(len(nevlista)):
    if len(nevlista[i]) > len(nevlista[index]):
        index = i

print ("A leghosszabb nevű ember a(z) ",index+1,". helyen van", sep="")
print("És az ő neve",nevlista[index])

#az indexessel el lehet érni a leghosszabbat is, másik ciklus nélkül