file = open("noveny.txt","r",encoding="utf8")
novenyek = []
for sor in file:
    novenyek.append(sor.strip())
file.close()



# 1. Írja ki a legrövidebb nevű növény fajtát!

legrovidebb = novenyek[0]

for i in novenyek:
    if len(i) < len(legrovidebb):
        legrovidebb = i

print("A legrövidebb nevű növény: ",legrovidebb)

for noveny in novenyek:
    if len(noveny) == len(legrovidebb):
        print("A legrövidebb nevű növény: ",noveny)

# *len() listánál hány elem, stringnél hány karakter



# 2.Írja ki azokat az növényeket, melyek fajtája legalább két szavas

print("Legalább 2 szóból álló növények:")
for noveny in novenyek:
    if " " in noveny:
        print(noveny)



# 3. Jelenítse meg azokat a növényeket, melyek fajtájában szerepel a „sás” kifejezés!

print("Fajtájában szerepel a „sás” kifejezés:")
for noveny in novenyek:
    if "sás" in noveny:
        print(noveny)


# 4. Jelenítse meg azokat a növényeket, melyek fajtája e vagy E betűvel kezdődik!

for noveny in novenyek:
    if noveny[0] == "e" or noveny[0] == "E":
    # VAGY if noveny[0].lower() == "e"
        print(noveny)



#5. Jelenítse meg azokat a növényeket, melyek fajtája e vagy E betűvel végződik!

for noveny in novenyek:
    if noveny[-1].lower() == "e":
    #if noveny[len(noveny)-1].lower() == "e":
        print(noveny)



# 6. Jelenítse meg azokat a növényeket, melyek fajtája e vagy E betűvel kezdődik és végződik!

for noveny in novenyek:
    if noveny[-1].lower() == "e" and noveny[0].lower() == "e":
        print(noveny)


# 7. Jelenítse meg, melyik növény fajtájában szerepel e vagy E betű?

for noveny in novenyek:
    if "e" in noveny.lower():
        print(noveny)


# 8. Olvasson be egy karaktert, majd jelenítse meg, melyik növény fajtájában szerepel a beolvasott karakter!

betu = input("Adj egy karaktert: ")

for noveny in novenyek:
    if betu.lower() in noveny.lower():
        print(noveny)


# 9. Minden növényfajt annyi karakteren jelenítsen meg a jobbra.txt fájlban, amennyi a leghosszabb fajtájú növény nevének hossza!

fileki = open("jobbra.txt","w", encoding="utf8")

leghosszabb = novenyek[0]
for noveny in novenyek:
    if len(noveny) > len(leghosszabb):
        leghosszabb = noveny

#hossz = len(leghosszabb)
#print(leghosszabb)
#print(hossz)

for noveny in novenyek:
    print(noveny.rjust(len(leghosszabb)))

for noveny in novenyek:
    fileki.write(noveny.rjust(len(leghosszabb)) + "\n")

fileki.close()



# 10. A kisbetus.txt fájlba másolja át az összes növény fajtáját csupa kisbetűvel megjelenítve!

fileki = open("kisbetus.txt","w",encoding="utf8")

for noveny in novenyek:
    fileki.write(noveny.lower() + "\n")

fileki.close()

# 11. A nagybetus.txt fájlba másolja át az összes növény fajtáját csupa nagybetűvel megjelenítve!

fileki = open("nagybetus.txt","w",encoding="utf8")

for noveny in novenyek:
    fileki.write(noveny.upper() + "\n")

fileki.close()



# 12. Kitalálós játék készítése
# a) Olvasson be egy számot! Ha a beolvasott szám nagyobb, mint ahány növény van, akkor írjon ki hibaüzenetet!

be = int(input("Adj meg egy számot: "))
sorszam = be

if be > len(novenyek):
    print("Nincs ennyi növény!")

# b) Keresse ki azt a sorszámú növényt, amelyiket a felhasználó megadott
print ("A(z) ",be,". növény: ",novenyek[be-1], sep="")
keresett = novenyek[be-1]
# print(lista[x-1])

# c)

#keresett = "Alacsony pozdor"

elso4 = keresett[:4]
utolso4 = keresett[-4:]
# utolso4v = keresett[ len(keresett) - 4:]

#print(elso4, end="")
#for i in range (len (keresett) - 8):
#    print(".", end="")
#print(utolso4, end="")


tippelendo = keresett [:4]

if len(keresett) >= 10:

    for i in range (4, len(keresett)-4):
        if keresett[i].isalpha():
            tippelendo += "."
        else:
            tippelendo += " "

    tippelendo += keresett [-4:]
else:
    tippelendo = keresett[0]+ "."*(len(keresett)-2) + keresett[-1]



print(tippelendo)


# d) 


kitalalta = False
for i in range (int(len (keresett) / 2)):

    usertipp = input("Add meg a tipped: ")

    if usertipp.lower() == keresett.lower():
        kitalalta = True
        break


if kitalalta == True:
    print("Nyertél!")
else:
    print("Vesztettél, a megoldás: ",keresett)
