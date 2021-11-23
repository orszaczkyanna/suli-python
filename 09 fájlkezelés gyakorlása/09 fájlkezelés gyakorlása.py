# 1. FELADAT    
# A filmek.txt fájl beolvasása, a címeket tároljuk el egy listában

f = open("filmek.txt","r", encoding="utf8")

filmek = []

#a sor ciklusváltozó minden iterációban felvesz az f fájlból egy új sort
#for sor in f:
#    filmek.append(sor)

# ez eleve úgy van leprogramozva, hogy soronként olvassa be, viszont a végére fűzi az entereket
# (másik verzió, hogy splitelem enterek mentén)

for sor in f:
    filmek.append( sor.strip() )

#sor.strip("a \n")
# eltávolítja a kis a, szóköz, enter karaktereket a végéről és elejéről

#string strip() metódusa: a string elejéről és végéről eltávolítja a nem látható karaktereket

f.close

#listázzuk ki a beolvasott lista tartalmát




for film in filmek:
    print (film)




# 2.FELADAT
# írassa ki, hogy hány film szerepel a listában
print("A fájlban", len(filmek) ,"darab film van.")


# 3. feladat
# Számold meg és írasd ki, hogy hány egyszavas filmcím van a listában
# listázd ki a legalább 5 szóból álló filmcímeket
# írj függvényt, amelyet mindkét feladatban tudsz használni
# ez a függvény lehet a szavak_szama()

def szavak_szama ( s ): # olyan nevet adjunk a függvénynek, hogy később egyértelmű legyen a funkciója
    darabolt = s.split(" ")
    return len(darabolt)

# print(szavak_szama("Teszt   sokszóköz"))
# Ha véletlen több szóközt ütök, akkor többnek számolja


egyszavasok = 0
for film in filmek:
    if szavak_szama(film) == 1:
        egyszavasok += 1
print("Az egyszavas címek száma: ", egyszavasok)


for film in filmek:
    if szavak_szama(film) >= 5:
        print (film)


# 4. feladat
# a) listázd ki azokat a film címeket, amelyek tartalmazzák a "három" szórészletet (akár kicsi, akár nagybetűvel)
# b) listázd ki azokat a filmcímeket, amelyek tartalmazzák a "három" szót (akár kicsi, akár nagybetűvel)
# c) olvass be a felhasználótól egy szót, szórészletet, majd listázd ki, azokat a filmeket, amelyek tartalmazzák azt (akár kicsi, akár nagybetűvel)
# írj praktikus függvényt, amit mindhárom részfeladatnál fel tudsz használni



print("\n\nNegyedik feladat\n")
def cimben_szoreszlet (cim, szoreszlet):
    if szoreszlet.lower() in cim.lower(): #a feltételben kell kisbetűssé alakítani
        return True
    else:
        return False #enélkül None-t ad

def cimben_szo (cim, szoreszlet):
    darabolt = cim.split(" ")
    for szo in darabolt:
        if szo.lower() == szoreszlet.lower():
            return True
    #csak akkor térjen vissza hamissal, ha miután végigment a címen sem talált egyezést
    return False

#tesztelés:
#print(cimben_szoreszlet("tizenhárom almafa","Három"))

print("\nAzon címeknek listája, amelyben a három szórészlet szerepel")
for film in filmek:
    if cimben_szoreszlet(film, "három"):
        print(film)

print("\nAzon címeknek listája, amelyben a három önálló szóként szerepel")
for film in filmek:
    if cimben_szo(film, "három"):
        print(film)

print()

szoreszlet = input("Adj meg egy szót, vagy szórészletet: ")

print("\nAzon címek listája, amelyben a",szoreszlet,"szórészlet szerepel")
for film in filmek:
    if cimben_szoreszlet(film,szoreszlet):
        print(film)

print("\nAzon címek listája, amelyben a",szoreszlet,"szó önálló szóként szerepel")
for film in filmek:
    if cimben_szo(film,szoreszlet):
        print(film)

# Írja ki azokat a filmeket, amelyekben egy adott szó, vagy szórészlet szerepel
# ez a szórészlet függvény



# 5. feladat
# olvass be egy betűt (karakter) a billentyűzetről, majd hozz létre egy szöveges fájlt, aminek a neve a beolvasott betű, és írd ebbe a fájlba, azokat a filmcímeket, amelyek ezzel a betűvel kezdődnek
# pl: "m" --> az m.txt állományba írja az m-mel kezdődő filmcímeket

betu = input("Adj meg egy betűt: ")

#.isalpha() lekezeli az ékezetes karakter
#.igaz, hamis értéket ad vissza. igaz ha betű, nem ha nem
# betu.isdecimal ugyanez csak számokra

if betu.isalpha() and len(betu) == 1:
    g = open(betu + ".txt","w", encoding ="utf8")

#a .lower() után feltétlen kellenek a zárójelek!!!
    for film in filmek:
        if film[0].lower() == betu.lower():
            g.write(film + "\n") # a write nem üt automatikusan entert, mint a print


    g.close
else:
    print("Nem egy darab karaktert adtál meg")



# 6.feladat
# írj programot, amely egy új szöveges fájlban, melynek neve: "filmcimhossz.txt" a filmek mellé írja, hogy hány karakter hosszúak, szóközzel körülvett kettősponttal elválasztva
# pl.: "A három kismalac" -> "A három kismalac : 16"


h = open("filmcimhossz.txt","w", encoding="utf8")

for film in filmek:
    h.write (film + " : " + str(len(film)) + "\n")

h.close()

# 7. kérjen be a felhasználótól egy számot, és írja ki az annyiadik sorszámú film címét
# az 1. film legyen az első film, ügyeljen arra, hogy érvénytelen sorszám ne legyen, azaz ne legyen nagyobb, mint amennyi film van az adatbázisban, és ne legyen kisebb, mint 1

# ha negatív számmal indexeljük a listát, akkor a lista végéről indexel, nincs alulindexelés (pl.: filmek[-1], filmek[-2])

sorszam = int(input("Adj meg egy sorszámot: "))
#ez is jó: if 0 < sorszam <= len(filmek):
if sorszam > 0 and sorszam <= len(filmek):
    print(sorszam,". film: ",filmek[sorszam - 1], sep="")
else:
    print("Érvénytelen sorszám")
