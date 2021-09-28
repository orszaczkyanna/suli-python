print("Hello World!")

x=12
y=14
print("Hello", "World", x, y)

print("Hello", "World", x, "éves vagyok")

#ctrl + F5
#program futtatása

print("Hello", end="")  #nem üt entert, mivel a sor vége üres
                        #\n = enter -> alapértelmezett end="\n"
print ("World")
print("Vezetéknév")
print("Keresztnév")


#\n  enter
#\t  vízszintes tabulátor
#\a  windows hangjelzés ??(\b) ??

print("Hello", end="\t")
print ("World")

print(1/3)
print( "A szám kerekítve: {0:.2f}".format (1/3) ) #formátumozó string

#0 -> az első
#elem
#tizedes pont után 2 karakter álljon


#!! kimaradt jegyzetek
print( "A szám kerekítve: {0:.2f}, a másik: {1:.4f}".format (1/3, 1/5))
print( "A szám kerekítve: {1:.2f}, a másik: {0:.4f}".format (1/3, 1/5))
print ("Kerekítve első: {0:.2f}, másik: {1:.4}".format(1/3, 1/7))

#régi típusú kiírás
print( "A szám kerekítve: %.2f, a másik: %.4f" % (1/3, 1/5))

x = 1/3
y = 1/7
print( "A szám kerekítve: %.2f, a másik: %.4f" % (x, y))


x = 5/2 #a változó az utolsó értéket hordozza magával, a későbbi érték felülírja a régebbit
print("x változó lecserélve")
print( "A szám kerekítve: %.2f, a másik: %.4f" % (x, y))


print ("1:3 = {0:.2f}".format (1/3))

#https://pyformat.info/
#https://www.w3schools.com/python/ (pontatlanságok)
#https://developer.mozilla.org/en-US/ - webfejlesztéshez jobb



x = input("Kérem a felhasználóneved: ")
print("Szia", x)

#szam = input("Kérek egy számot: ") #input alapértelmezetten string


szam = int (input("Kérek egy számot: "))
#Az int a beolvasott értékre vonatkozik, nem az eredményre. Megadni nem tudok tizedes törtet.
#szam = float (input("Kérek egy számot: "))
print("A szám fele: ", szam/2)







#Kérd be a felhasználótól az aktuális időt (csak az órát)
#majd kérd be azt is, hogy hány óra múlva szólaljon meg az ébresztő
#a prog írja ki, hogy mikor szól az ébresztő

aktid= int (input ("Add meg az aktuális időt:  "))
plusz= int(input("Hány óra múlva szóljon az ébresztő?  "))
print("Az ébresztő ekkor szól: ", (aktid+plusz) % 24 )


#bekérni téglalap 2 oldalának hossza
#kiírni: kerület, terület
#K=  2*(a+b)
#T=  (a*b)

a = int (input("Add meg a téglalap 'a' oldalát: "))
b = int (input("Add meg a téglalap 'b' oldalát: "))
print("A téglalap kerülete: ", 2*(a+b))
print("A téglalap területe: ", a*b)


#3szög oldalainak hossza
# T = füzetben

import math #innen tudunk a matematikai függvényekre hivatkozni
#math.sqrt(25) #meghatározza a 25 négyzetgyökét
print (math.sqrt(25))


a = int (input("Add meg a háromszög 'a' oldalát: "))
b = int (input("Add meg a háromszög 'b' oldalát: "))
c = int (input("Add meg a háromszög 'c' oldalát: "))
k = a+b+c 

s = k/2
T = math.sqrt(s*(s-a)*(s-b)*(s-c))


print("s érték: ", s)
print("A háromszög kerülete: ", k)
print("A háromszög területe: ", T)


x = 25
print(x)
print("a változó típusa: ", type(x)) #változó típusának kiíratása




# határozzuk meg egy számról, hogy páros-e
# ha.... akkor utasítás(oka)t
#ha <feltétel> akkor [utasítás]

#if <feltétel>:
#   [utasítás]



szam= int (input("Kérek egy számot: "))

if szam % 2 == 0:
    print("A szám páros") #törzs - behúzás után
    print ("vége a programnak")
else:
    print("A szám páratlan")

print ("most van valójában vége a programnak")



# egy szám negatív vagy pozitív

szam= int (input("Kérek egy számot: "))

if szam >= 0:
    print("A szám pozitív")
else:
    print("A szám negatív")





if szam > 0:
    print("A szám pozitív")
elif szam < 0:
    print("A szám negatív")
else:
    print("a szám nulla")






#érdemjegyek

a = int(input("Add meg az érdemjegyed: "))

if a == 5:
    print("A jegyed 5-ös")
elif a == 4:
    print("A jegyed 4-es")
elif a == 3:
    print("A jegyed 3-as")
elif a == 2:
    print("A jegyed 2-es")
elif a == 1:
    print("A jegyed 1-es")
else:
    print("Érvénytelen osztályzat")




# bekért szám, ha pozitív és nagyobb mint 10 akkor 'ügyes vagy'

jegy = int(input("Írj be egy számot: "))
if jegy > 0:
    if jegy == 10:
        print("Ügyes vagy")
    print("A szám pozitív")




jegy = int(input("Írj be egy számot: "))
if jegy>0 and jegy>10:
    print("ügyes vagy")


# be - születési évszám határozd meg az életkort
# ha szül.év kisebb, mint a 1900 vagy több mint 2021 akkor 'Nem valós születési év'
# egyébként írja ki, hány éves

szul = int(input("Add meg a születési évedet: "))

if szul < 1900 or szul > 2021:
    print("Nem valós születési év")
else:
    print(2021-szul, "éves vagy")

