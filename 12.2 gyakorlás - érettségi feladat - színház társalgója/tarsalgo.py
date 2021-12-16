# Az első két szám az áthaladás időpontja (óra, perc),
# a harmadik a személy egyedi azonosítója,
# az utolsó az áthaladás iránya (be/ki)

class Szineszek_BeKiLepes:
    def __init__ (self, sor):
        darabolt = sor.split(" ")
        self.ora = int(darabolt[0])
        self.perc = int(darabolt[1])
        self.azonosito = int(darabolt[2])
        self.beki = darabolt[3]

class Hanyszor_KiBe:
    def __init__ (self,a,b):
        self.kib_azonosito = a
        self.kib_hanyszor = b

# 1. feladat
kibelista = []

f = open("ajto.txt","r",encoding="utf8")

for sor in f:
    uj = Szineszek_BeKiLepes(sor.strip())
    kibelista.append(uj)    

f.close()

# 2. feladat
print("\n2. feladat:")
print("Az első belépő:",kibelista[0].azonosito)
print("Az utolsó kilépő:",kibelista[len(kibelista)-1].azonosito)

# 3. feladat
osszes_azonosito = []

for i in range(len(kibelista)):
    egyazon = kibelista[i].azonosito
    osszes_azonosito.append(egyazon)

azonositok = [osszes_azonosito[0]]

for i in osszes_azonosito:
    if i not in azonositok:
        azonositok.append(i)

athaladas = []
for j in range(len(azonositok)):
    azz = azonositok[j]
    hanyszor = 0
    for i in range(len(kibelista)):
        if azz == kibelista[i].azonosito:
            hanyszor += 1
    uj = Hanyszor_KiBe(azz,hanyszor)
    athaladas.append(uj)

f2 = open("athaladas_rendezetlen.txt","w",encoding="utf8")
for j in range(len(athaladas)):
    f2.write(str(athaladas[j].kib_azonosito)+" "+str(athaladas[j].kib_hanyszor)+"\n")
f2.close()

rendezett_athaladas = sorted(athaladas, key=lambda x: x.kib_azonosito)

f2 = open("athaladas.txt","w",encoding="utf8")
for j in range(len(rendezett_athaladas)):
    f2.write(str(rendezett_athaladas[j].kib_azonosito)+" "+str(rendezett_athaladas[j].kib_hanyszor)+"\n")
f2.close()

# 4. feladat
print("\n4. feladat:")

akikbennmaradtak = []
for i in azonositok:
    bemennyi = 0
    kimennyi = 0
    for j in range(len(kibelista)):
        if kibelista[j].azonosito == i:
            if kibelista[j].beki == "be":
                bemennyi += 1
            else:
                kimennyi += 1
    if bemennyi > kimennyi:
        akikbennmaradtak.append(int(i))

benn = sorted(akikbennmaradtak)
print("A végén a társalgóban voltak:",benn)
