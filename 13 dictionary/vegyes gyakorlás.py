# 1. Írj programot, amely beolvas két egész számot, majd kiírja két tizedesjegy pontossággal a nagyobb és kisebb szám hányadosát, az alábbi példa szerint:
# Ha a kisebb szám 0, akkor az 'osztás nem végezhető el' üzenet jelenjen meg eredményként:
# pl.: első szám: 14, második: 3, kimenet: 14 : 3 = 4.67

a = int (input("Add meg az egyik számot: "))
b = int (input("Add meg a másik számot: "))

# v1
if a < b:
    nagyobb = b
    kisebb = a
else:
    nagyobb = a
    kisebb = b

# v2 
if b > a:
    seged = b  # először a seged kell --> vödör példa
    b = a
    a = seged

if b != 0:
    #eredmeny = a / b
    #print(a,":", b, "= {0:.2f}".format(eredmeny)) # a vessző szeparátor alapértelmezetten szóköz
    print("{0} : {1} = {2:.2f}".format(a, b, a/b))
else:
    print("Az osztás nem végezhető el")



# 2. feladat: Írj programot, mely addig olvas be számokat míg a bemenet 0 nem lesz,
# majd kiírja egymás mellé, egy sorba, tabulátorral elválasztva a páros számokat, egy másik sorba pedig a páratlan számokat!
# Írja ki továbbá az összes megadott szám átlagát 4 tizedes jegyre kerekítve,
# valamint a legnagyobb páros számot és a legkisebb páratlan számot, ha van!

be = int(input("Adj egy számot: "))
parosok = []
paratlanok = []

if be != 0:        
    while be != 0:    # itt is hozzáadogathatom az átlagszámításhoz
        if be % 2 == 0:
            parosok.append(be)
        else:
            paratlanok.append(be)
        be = int(input("Adj még egy számot: "))

    print("Páros számok: ",end="\t")
    for i in parosok:
        print (i, end="\t")
    print("\nPáratlan számok: ",end="\t")
    for i in paratlanok:
        print (i, end="\t")

    osszeg = 0
    for i in parosok:
        osszeg += i
    for i in paratlanok:
        osszeg += i

    # ezt, ha eleve feltételhez kötöm akkor nem kell
    if len(parosok) != 0 and len(paratlanok) != 0:
        atlag = osszeg / (len(parosok) + len(paratlanok))
        print ("\nAz összes megadott szám átlaga 4 tizedesjegyre kerekítve: {0:.4f}".format(atlag))

    # Ezt itt mindenképp vizsgálni kell
    if len(parosok) != 0:
        print("\nA legnagyobb páros szám:",max(parosok))
    if len(paratlanok) != 0:
        print("\nA legkisebb páratlan szám:",min(paratlanok))
    
else:
    print("Nullát adtál meg")