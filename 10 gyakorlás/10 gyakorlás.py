

# Írj programot, amely kiírja az összes 9-cel osztható kétjegyű pozitív számot
# 18, 27, 36....


print("\nEgyik verzió:")
for i in range (10,100):
    if i % 9 == 0:
        print (i,end=" ")

print("\n\nMásik verzió:")
for i in range (18, 100, 9):
    print (i, end=" ")

print("\n\nHarmadik verzió:")
i = 10
while i <= 99:
    if i % 9 == 0:
        print (i, end=" ")
    i += 1


print("\n\nNegyedik verzió:")
i = 18
while i <= 99:
    print (i, end=" ")
    i += 9


# 2. While ciklus segítségével írd ki a képernyőre az első 10 pozitív egész szám négyzetét


print("\n\n 2. feladat")
i = 1
while i <= 10:
    print (i**2, end=" ")
    i += 1


# pdf 1.feladat
# Írj olyan programot, amelynek egy család tagjainak életkorát megadva, kimenetként kiírja a család átlagéletkorát.
# A bemenet végét nulla jelzi.
# Az átlagot 2 tizedesjegy pontossággal kell kiírni a szabványos kimenetre.
# Ha 0-n kívül más bemenet nem volt megadva, írja ki, hogy "Nem volt bemenet."

csaladtagok_szama = 0
osszeseletkor = 0
eletkor = int(input("\n\nAdd meg az életkorod!  "))

if eletkor != 0:
    while eletkor != 0:
        osszeseletkor += eletkor
        csaladtagok_szama += 1    
        eletkor = int(input("Add meg az életkorod!  "))
    
    #print(eletkor, csaladtagok_szama, osszeseletkor, sep=",   ")

    print ("Az átlag életkor {0:.2f}".format(osszeseletkor/csaladtagok_szama))
else:
    print ("Nem volt bemenet.")


# x1,y1;x2,y2
# N szám

# import math

N = int(input("Hány téglalapot dolgozzak fel? "))



for i in range (N):
    
    beolvas = input("Kérek egy koordinátát: ")
    koordinatak = beolvas.split(";")
    #print(koordinatak)
    also_koordinatak = koordinatak[0].split(",")
    felso_koordinatak = koordinatak[1].split(",")

    #print (also_koordinatak)
    #print (felso_koordinatak)

    x_also = int(also_koordinatak[0])
    y_also = int(also_koordinatak[1])
    x_felso = int(felso_koordinatak[0])
    y_felso = int(felso_koordinatak[1])

    a = abs( x_felso - x_also )
    b = abs( y_felso - y_also )
    T = a*b
    print("T = ",T)





# pdf 3.feladat
print ("\npdf 3. feladat\n")

def adokedvezmeny (szelesseg, hosszusag, ado):
    if szelesseg <= 15 or hosszusag <= 25:
        return ado * 0.8
    else:
        return ado

#pass

print (adokedvezmeny(20, 30, 10000))
print (adokedvezmeny(15, 30, 10000))
print (adokedvezmeny(20, 24, 10000))



# pdf 4.feladat

print ("\npdf 4. feladat\n")
def dijazas (ut_hossza):
    if 1 <= ut_hossza <= 2:
        return 500
    elif 3 <= ut_hossza <= 5:
        return 700
    elif 6 <= ut_hossza <= 10:
        return 900
    elif 11 <= ut_hossza <= 20:
        return 1400
    elif 21 <= ut_hossza <= 30:
        return 2000


print(dijazas(2))
print(dijazas(30))





# pdf 5.feladat
print ("\npdf 5. feladat\n")


honapok = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
datum = input ("Adj meg egy dátumot: ")
darabolt = datum.split(".")
honap = int (darabolt[1])
nap = int (darabolt [2])

# hanyadiknap = 0
# Meghatározom, hogy a beadott hónap előtti hónapok összesen hány napot tartalmaznak.
# (pl.: március esetén összeadom a jan és febr hónapok napjainak számát)

# for i in range (honap): #ha januárt adok meg, nem fog lefutni, marad a nap szám
#     hanyadiknap += honapok[i]
# hanyadiknap += nap

#3 hónap -> 2-ig veszi bele, tehát a 0, és 1, ami a jan és a feb
# másik:
for i in range (honap): #ha januárt adok meg, nem fog lefutni, marad a nap szám
    nap += honapok[i]

print(nap)


# maradékosztás->
# ha elosztom 7-tel, hogy a hét hanyadik napjáról van szó, megkapom a maradékot
# tudnom kell, hogy az 1-es milyen nap volt, a többit ahhoz igazítom


if nap % 7 == 1:
    print ("péntek")
elif nap % 7 == 2:
    print ("szombat")
elif nap % 7 == 3:
    print ("vasárnap")
elif nap % 7 == 4:
    print ("hétfő")
elif nap % 7 == 5:
    print ("kedd")
elif nap % 7 == 6:
    print ("szerda")
elif nap % 7 == 0:
    print ("csütörtök")



# 6. pdf

print("6. pdf feladat")

szo = input ("Adj meg egy szót: ")
szo_forditva = szo[::-1] #rész-string fordított bejárással 

if szo == szo_forditva:
    print("Ez egy palindrom szó")
else:
    print("Ez nem egy palindrom szó")


# 7. pdf

print("7. pdf feladat")

def palindromszo (szo):
    szo_forditva = szo[::-1]
    if szo == szo_forditva:
        return True
    else:
        return False


def palindromszo2 (szo):
    if szo == szo[::-1]:
        return True
    else:
        return False
    

def palindromszo3 (szo):
    return szo == szo[::-1]
# azt fogja visszaadni, hogy a feltétel igaz, vagy hamis 
