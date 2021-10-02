# 1. feladat
mat = int ( input( "Add meg a matematika jegyed: " ))
ang = int ( input ("Add meg az angol jegyed: "))
inf = int ( input ("Add meg az informatika jegyed: "))

print ("A jegyeid átlaga: ", (mat + ang + inf)/3)

# 2. feladat
benz = int (input ("Hány liter benzin van a tankban? "))
fogy = int (input ("Mekkora az autó átlagos fogyasztása? "))

print("Még ",100*benz/fogy,"km-t tud megtenni")

# 3. feladat
pontsz = int (input ("Add meg, hány pontot szereztél: "))
pontm = int (input("Add meg mennyi a maximum elérhető pontszám: "))

if pontsz/pontm*100 >= 60:
    print ("Sikeresen vizsgáztál")
else:
    print ("A vizsga sikertelen")

# 4. feladat
mag = float (input ("Add meg a magasságod cm-ben: "))
suly = float (input ("Add meg a súlyod kg-ban: ")) 

bmi = suly/((mag/100)**2)
bmi2 = "{0:.2f}".format (bmi)

if bmi < 18.5:
    print ("A testtömegindexed ",bmi2," , azaz sovány vagy.")
elif bmi >= 18.5 and bmi < 25:
    print ("A testtömegindexed ",bmi2," , azaz normál testsúlyú vagy.")
else:
    print ("A testtömegindexed ",bmi2," , azaz túlsúlyos vagy.")

# 5. feladat
evszam = int (input ("Adj meg egy évszámot: "))
if evszam%4==0:
    print (evszam,"szökőév.")
else:
    print (evszam,"nem szökőév.")
