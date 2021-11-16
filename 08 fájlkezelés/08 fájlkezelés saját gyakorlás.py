#Első feladat
def oszto (szam):
    #szam = 1
    osztok = 0
    for i in range (1,szam+1):
        if szam % i == 0:
            osztok += 1
    return osztok

#próbálkozás:
szamok = []
legtobb = 0
for i in range (5):
    szamm = int(input("Adj meg egy pozitív egész számot: "))
    szamok.append(szamm)
    print(szamm,"osztóinak száma",oszto(szamm))
    if oszto(szamm) > oszto(legtobb):
        legtobb = szamm
    
print ("A legtöbb osztója ezeknek a számoknak van: ")
for i in range (len(szamok)):
    if oszto(szamok[i]) == legtobb:
        print(szamok[i])

