class Adat:
    def __init__ (self, szoveg):
        darabolt = szoveg.split(";")
        self.ora = int(darabolt[0])
        self.perc = int(darabolt[1])
        self.db = int(darabolt[2]) # hány hívás az adott percben
        self.nev = darabolt[3]

    def kiir (self):
        return str(self.ora) + " : " + str(self.perc) + "-kor " + str(self.db) + "db hívás, név:" + self.nev




adatok = []

# működik-e az Adat osztály
# probataxis = Adat("18;2;3;Jani")
# print(probataxis.nev, probataxis.ora, probataxis.perc, probataxis.db)

f = open("cb.txt","r",encoding="utf8")

elsosor = f.readline() # így a for már a másodiktól indul
for sor in f:
    uj = Adat(sor.strip())
    adatok.append(uj)

f.close()



print("3. feladat: ", end="")
print("Bejegyzések száma: ", len(adatok))

print("\n4. feladat: ", end="")
vane = False
for i in range(len(adatok)):
    if adatok[i].db == 4:
        vane = True
        break
if vane:
    print("Volt négy adást indító sofőr")
else:
    print("Nem volt négy adást indító sofőr")  


#for i in range (len(adatok)):
#    print(adatok[i].kiir())



print("\n5. feladat: ", end="")
nev = input("Kérek egy nevet: ")
hivasok = 0
for taxis in adatok:
    if taxis.nev.lower() == nev.lower():
        hivasok += taxis.db
if hivasok != 0:
    print("\t {0} {1}x használta a CB-rádiót".format(nev, hivasok))
else:
    print("\tNincs ilyen nevű sofőr!")




# 6. feladat
# ha a feladat szövege paraméterről ír, akkor (valószínűleg) külön függvény kell
def AtszamolPercre (ora, perc):
        return 60*ora + perc

# 7. feladat

f = open("cb2.txt","w",encoding="utf8")
f.write("Kezdés;Nev;Adasdb\n")

for taxis in adatok:
    f.write("{0};{1};{2}\n".format(AtszamolPercre(taxis.ora,taxis.perc), taxis.nev, taxis.db  ))

f.close()


# 8. feladat

nevek = []
for taxis in adatok:
    if taxis.nev not in nevek:
        nevek.append(taxis.nev)
print("8. feladat: sofőrök száma {0} fő".format(len(nevek)))


# 9. feladat

szotar = {}
for taxis in adatok:
    if taxis.nev not in szotar.keys():
        szotar.update( {taxis.nev : taxis.db} )
    else:
        szotar[taxis.nev] += taxis.db


# a kulcsokat járja be
for sz in szotar:
    print(sz)

# a kulcsokkal le tudom kérni az értékeket:
for sz in szotar:
    print(sz, szotar[sz])


legtobbhivas = 0
legtobbtaxis = ""

for sz in szotar:  # táblázat első oszlopát, kulcsait járja be
    if szotar[sz] > legtobbhivas: # []-val lekérem az értéket
        legtobbtaxis = sz # a sofőr név a kulcs
        legtobbhivas = szotar[sz] # az érték a hívások száma

print("9. feladat: a legtöbb hívást indító sofőr")
print("\tNév:", legtobbtaxis)
print("\tAdások száma:",legtobbhivas,"alkalom")