# 1. feladat: Páratlan számok 1 és 199 között
for i in range(1, 200, 2):
    print(i)

# 2. feladat: A 3 szorzatai 1-től 50-ig
for i in range(1, 51):
    print(i * 3)

# 3. feladat: Az 5 többszörösei 10 és 95 között
for i in range(2, 20):
    print(i * 5)

# 4. feladat: 2 hatványai 1-től 10-ig
for i in range(1, 11):
    print(2 ** i)

# 5. feladat: Jobbra lépcsőző csillagok
space = ""
for i in range(5):   
    print(space + "*")
    space += " "

# 6. feladat: 10 jegy átlaga
osszeg = 0
for i in range(10):
    jegy = int(input("Add meg a jegyed: "))
    osszeg += jegy
print("Átlag:", osszeg / 10)

# 7. feladat: 10 szám: összeg, páros darab, legnagyobb
osszeg = 0
paros = 0
legnagyobb = 0

print("Adj meg 10 pozitív egész számot!") 
for i in range(1, 11):
    print(i, end=". ")
    szam = int(input())
    if szam >= 0:
        osszeg += szam
        if szam % 2 == 0:
            paros += 1
        if szam > legnagyobb:
            legnagyobb = szam

print(paros, "szám páros")
print("A számok összege:", osszeg)
print("A legnagyobb szám:", legnagyobb)
