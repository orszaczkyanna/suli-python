#string kezelés
s1 = "alma"
s2 = "fa"

print ( s1 + s2 )
s3 = s1 + s2 #string konkatenáció, összefűzés (concatenation)
print (s3)



# string konkrét karakterének elérése
print (s1[0]) #"alma" string 0. (első) karaktere

print ("Az s1 string hossza:", len(s1)) #string hossza (4)

print("Az s1 utolsó betűje: ", s1[ len(s1) - 1] ) #string utolsó karakterének elérése



#utolsó elem: a hossz -1
#s1 string változó utolsó karaktere: s1[ len(s1) - 1] )


#lista = ["Teszt"]
#lista [len(lista) - 1]
#print ("valami",lista [len(lista) - 1]) Valami nem jó

#karakterenként írd ki a stringet
for i in s1:
    print (i)

#while ciklussal
i = 0
while i < len (s1):
    print (s1[i])
    i += 1





#Rész-stringek

s = "paralelepipedon"
s1 = s[2:6] 
#kettest beleveszi 6-os már nem
#eleje benne van, vége már nincs
print("s rész-stringje: ", s1)

s2 = s[2:] # 2-es indextől végig képzi a stringet (2index - 3mas)
#s2 = s[ 2:len(s) ]
print("s másik rész-stringje: ", s2)

s3 = s[:6] # a string elejétől az 5. indexel bezárólag a stringet
#a3 = s[0:6]
print("s harmadik rész-stringje: ", s3)




#egy karakter benne van-e egy stringben
if "a" in s: # ha 'a' karakter benne van az 's' stringen
    print("benne van a betű")
else:
    print("nincs benne")



#egy rész-string benne van-e egy másik stringben

if "lele" in s:
    print ("a feltételben lévő rész benne van")
else:
    print ("a feltételben lévő rész nincs benne")


if "sas" in s:
    print ("a feltételben lévő rész benne van")
else:
    print ("a feltételben lévő rész nincs benne")



# lecserélni a string első betűjét más nyelvben:
# s [0] = "X"
# pythonban nem, helyette:
s_uj = "X" + s[1:]
print("az első karakter módosítása után:",s_uj)


#a stringben minden 'a' betűt cseréljünk le '-'-re (kötőjelre)

skot = ""
#a skot változóba felveszi az s string karaktereit a feltétel alapján
for i in s: 
    if i == "a":
        skot += "-"
    else:
        skot += i 
print("a betűmentes változat:",skot)



skot2 = s.replace("a","-")
#melyik karakterét mire
#új változóba 
print("segédfüggvénnyel:", skot2)

#ha elkezdem, hogy s. felajánlja a segédfüggvényeket
print ("nagybetűs:", s.upper())
#s.lower() #kisbetűssé alakít


#első betű nagybetű s.capitalize()
#függvények után mindig karakter zárójelek, ha nincs paramétere, üres zárójelek



#Olvassunk be egy szót és a magánhangzókat cseréljük le '_' alsó vonalra

szo = input("kérek egy stringet: ")
szo = szo.lower()
seged = ""

for i in szo: # az i felveszi a "szo" karaktereit
    if i in "aáeéiíoóöőuúüű": #az i benne van-e a stringben
        seged += "_"
    else:
        seged += i

print ("Magánhangzó mentes szó:",seged)



#vezetéknév keresztév - monogram

vezetek = input("Vezetéknév: ")
kereszt = input("Keresztnév: ")

print (vezetek[0] + kereszt[0])


# egy változóba szóközzel

nev = input("Add meg a neved: ")
szokot_helye = 0 #!
nevmasolat = nev # ha az eredeti verzióval akarok dolgozni

while "  " in nev:
    nev = nev.replace("  "," ") # két szóközt egyre cserél, amíg dupla szóköz van bárhol


if " " in nev:
    for i in nev:
        if i == " ":
            break
        else:
            szokot_helye += 1

    monogram = nev[0] + nev [szokot_helye + 1] # szóköz után karakter [szokot_helye + 1]
    print ("A monogram:",monogram)
else:
    monogram = nev[0]
    print ("A monogram:",monogram)

#szóközök száma, szavak száma eredetiben

szokozszam = 0
for i in nevmasolat:
    if " " == i:
        szokozszam += 1
print("Eredetileg beírtban szóközök száma: ",szokozszam)


szavak = 0
for i in nev:
    if " " == i:
        szavak += 1
print(szavak+1, "szót írtál be")




szolista = nev.split (" ") # név stringet feldarabolja szóközök mentén és beleteszi a 'szolista' listába
print(szolista)
print ("A szavak száma:", len(szolista))


#Több név esetén monogram

nev = input("Add meg a neved: ")

while "  " in nev:
    nev = nev.replace("  ", " ")

darabok = nev.split(" ") # szóköz mentén spliteli

monogram = "" #induló érték

for i in darabok:
    monogram += i[0]

print (monogram)
print ("Az egyes névrészek: ", darabok)



#lista = []
#lista = [ 3,6,10,8,25 ]
lista = [ -3,-6,10,-8,-25 ]
# alapvető programozási tételek:

#legnagyobb = 0 -> mínusz számok esetében a nulla lesz a legnagyobb
# listában nem szereplő elemmel hasonlít össze
legnagyobb = lista[0] #Listán belüli elemeket hasonlítsa össze

for i in lista:
    if i > legnagyobb:
        legnagyobb = i
print ("Lista legnagyobb eleme:",legnagyobb)

print("legnagyobb elem függvénnyel: ", max(lista))
print("legkisebb elem függvénnyel: ", min(lista))