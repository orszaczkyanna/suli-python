class Dolgozo:

    def __init__(self, sor):    #ez lefut, amikor létrehozok egy példányt
        darabolt = sor.split("\t")
        self.azonosito = darabolt[0]  #az "azonosito" egy _adattag_
        self.oradij = int( darabolt[1] )
        self.munkaora = int( darabolt[2] )
    
    def kiir_dolgozo(self):
        return "Név: " + self.azonosito + ", óradíj: " + str(self.oradij) + ", munkaóra: " + str(self.munkaora)

    def fizetes(self):
        kalkulacio = (4 * self.munkaora * self.oradij) * 0.67
        return kalkulacio



    
fajl = open("fizu.txt", "r", encoding="utf8")
dolgozok = [] # a listába objektumok kerülnek, amik adattagokkal rendelkeznek
for sor in fajl:
    ujdolgozo = Dolgozo( sor.strip() ) # konstruktor lefut (init), ((amikor az osztály nevét így megadom,, a konstruktor egy sort tud feldolgozni))
    dolgozok.append(ujdolgozo)
fajl.close()

# a fájl beolvasása megtörtént

#for d in dolgozok:
#    print(d.kiir_dolgozo())


# dolgozo1 = Dolgozo("VM03F\t2000\t20")
# print (dolgozo1.azonosito, dolgozo1.oradij, dolgozo1.munkaora)

"""
# b)

print("\nB) rész")
print(len(dolgozok),"dolgozó szerepel a fájlban")


# c)

print("\nC) rész")
osszeg = int (input("Kérek egy óradíjat: "))
szamlalo = 0
for d in dolgozok:
    if d.oradij > osszeg:
        szamlalo += 1
print(szamlalo,"személynek magasabb ennél az óradíja")

"""

# d)

print("\nD) rész")
for d in dolgozok:
    if d.munkaora < 15:
        print (d.azonosito)

# e)
print("\nE) rész")
osszeg = 0
darab = 0
for d in dolgozok:
    if d.azonosito[-1].upper() == "N":
        osszeg += d.munkaora
        darab += 1
#print("A női dolgozók átlagosan", int(osszeg/darab) ,"órát dolgoznak hetente")
print("A női dolgozók átlagosan {0:.2f} órát dolgoznak hetente".format(osszeg/darab))

# f)
print("\nF) rész")
legnagyobb_oradij = dolgozok[0].oradij
legnagyobb_azonosito = dolgozok[0].azonosito
vaneferfi = False

for d in dolgozok:
    if d.azonosito[-1] == "F":
        legnagyobb_azonosito = d.azonosito
        legnagyobb_oradij = d.oradij
        vaneferfi = True
        break

for d in dolgozok:
#if d.azonosito[-1].upper() == "F":
    if d.oradij > legnagyobb_oradij and d.azonosito[-1].upper() == "F":
        legnagyobb_oradij = d.oradij
        legnagyobb_azonosito = d.azonosito



if vaneferfi:
#if vaneferfi == True:
    print("A legnagyobb óradíjjal dolgozó férfi azonosítója:",legnagyobb_azonosito)
else:
    print("Nincs férfi alkalmazott a cégnél")


# G)
print("\nG) rész")


# classban:
#def fizetes(self):
#    kalkulacio = (4 * self.munkaora * self.oradij) * 0.67
#    return kalkulacio

"""
for d in dolgozok:
    print (d.kiir_dolgozo() + " fizetése " + str(d.fizetes()) )

"""

def fizetes (oradij, hetimunkaora):
    return (4*hetimunkaora*oradij)*0.67

print ("Példa havi fizetés (4 óra hetente, 2500Ft óránként)", fizetes (2500,4))

# A classban lévőt nem kell paraméterezni, és csak példányra lehet meghívni, így külön nem
# a classosnál nem tudok megadni példaértéket

"""
# H)
print("\nH) rész")

monogram = input("Adj meg egy monogramot: ")

for d in dolgozok:
    if d.azonosito[:2] == monogram:
        print(d.azonosito,"fizetése",int(fizetes(d.oradij, d.munkaora)))

"""
# I)
print("\nI) rész")

osszesfizetes = 0
dolgozokszama = 0 #len(dolgozok)

for d in dolgozok:
    osszesfizetes += fizetes(d.oradij, d.munkaora)
    dolgozokszama += 1
print("A dolgozók havi átlagfizetése:", osszesfizetes/dolgozokszama)


# J)
print("\nJ) rész")

legnagyobb_fizetes = dolgozok[0].fizetes()
legnagyobbsorszam = 0
aktualissorszam = 0

for d in dolgozok:
    if d.fizetes() > legnagyobb_fizetes:
        legnagyobb_fizetes = d.fizetes()
        legnagyobbsorszam = aktualissorszam
    aktualissorszam += 1

print("A legmagasabb fizetésű személy sorszáma:", legnagyobbsorszam + 1)