

# pdf 8 - palindrom mondat-e, angol abc kisbetűi
bemenet = input("Kérek egy mondatot: ")
tisztitott = ""



for betu in bemenet:
    #betu = betu.lower()
    if betu.isalpha():       #!zárójelek!
        tisztitott += betu
    
#print(bemenet)
#print(tisztitott)

kisbetus = tisztitott.lower()



if kisbetus[::-1] == kisbetus:
    print("Palindrom: ",bemenet)
else:
    print("Nem palindrom")


# 9. pdf: függvény(ek) palindrom prím-e
# 1v - saját

def palindromprim (szam):
    osztokszama = 0
    for i in range (1, szam):
        if szam % i == 0:
            osztokszama += 1
    
    sztring = str(szam) 

    return osztokszama == 1 and sztring == sztring[::-1]




teszt = int(input("Adj egy számot: "))

if palindromprim(teszt) == True:
    print("Prím palindrom")
else:
    print("Nem prím palindrom szám")


#9. v2 - közös

def palindromszo3 (szo):
    return szo == szo[::-1]

def primszam (szam):
    for i in range (2,szam):
        if szam % i == 0:
            return False
    return True

def palindromprim (szam):
    return palindromszo3(str(szam)) and primszam (szam)


bemenet = int(input ("Kérek egy számot: "))

if palindromprim(bemenet):
    print("A szám palindrom prím.")
else:
    print("A szám nem palindrom prím.")




