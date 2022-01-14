from os import write

# 1. feladat
print("1. feladat")
f = open("melyseg.txt", "r", encoding="utf8")
melyseg = []
for i in f:
    uj = i.strip()
    melyseg.append(int(uj))
f.close()
print("A fájl adatainak száma:", len(melyseg))

# 2. feladat
print("\n2. feladat")
tavolsagertek = int(input("Adjon meg egy távolságértéket! "))
print("Ezen a helyen a felszín {0} méter mélyen van.".format(melyseg[tavolsagertek-1]))

# 3. feladat
print("\n3. feladat")
nullak = 0
for i in melyseg:
    if i == 0:
        nullak += 1

szazalek = nullak / len(melyseg) * 100
print("Az érintetlen terület aránya {0:.2f}%.".format(szazalek))

# 4. feladat
f = open("godrok.txt","w", encoding="utf8")
for i in range(len(melyseg)):
    if melyseg[i] != 0:
        f.write(str(melyseg[i]) + " ")
    elif melyseg[i-1] != 0:
        f.write("\n")
f.close()

# 5. feladat
print("\n5. feladat")

f = open("godrok.txt","r", encoding="utf8")
godrok = []
for i in f:
    godrok.append(i.strip())
f.close()

print("A gödrök száma:",len(godrok))

# 6. feladat
print("\n6. feladat")
if melyseg[tavolsagertek-1] == 0:
    print("Az adott helyen nincs gödör")
else:
    print("A 6. feladat nincs befejezve")
