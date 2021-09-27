# egysoros megjegyzes

"""

tobbsoros megjegyzes
ha nem akarok minden sor elejere
#-t tenni

"""

print("Hello World!")

print("Hello World!2");

print("Hello World!3");

# literal
# felirasi modja hatarozza meg a 
# tipusat

# egesz szam
print(42)

print( 42 + 42 )

# string, karakterlanc, karakterfuzer
print("42")

print("42 + 42")

# valos szam
print(38.45)

# egesz : integer
print(  type( 42  )      )

# valos: float
print(  type( 38.75  )      )

# string: str
print(   type("hello") )

print( "hello" + "world")
print( "42" + "42")


print( 42 * 42 )
print( 42 / 42 )

# elteres a python verziok kozott!!!

print( "15/4=" )
print( 15/4 )
print( "15.0/4=" )
print( 15.0/4 )

print( 15//4 )

# valtozo deklaracioja

valtozo = 15

print( valtozo  )

valtozo = 20

print( valtozo  )

valtozo = 32 + 64

print( valtozo  )

a = 10
b = 15

c = (a + b)/2
print("az a valtozo erteke: ")
print( a )
print("a b valtozo erteke: ")
print( b )
print("a c valtozo erteke: ")
print( c )

# hatvanyozas

print( 2**4 )

# maradekkepzes

print( 14%4 )

valtozo = "szoveg"

print( valtozo*3)

#be = input("Kerem a bemeno adatot")

# a konzolrol bekersz ket szamot egy-egy valtozoba, es kiiratod az osszeguket, kulonbseguket, szorzatukat, hanyadosukat

# konverzio

valtozo = int( "13" )


print("Kerek majd ket szamot")

#elso = int( input("kerem az elso szamot:") )

#masodik = int(input("kerem a masodik szamot"))
"""
print(" a ket szam osszege:")
print( elso + masodik )
print( "a ket szam kulonbsege:")
print( elso - masodik )
print( "a ket szam hanyadosa:")
print( elso / masodik )
print( "a ket szam szorzata:")
print( elso * masodik )
"""

"""

hozzatok letre 3 valtozot

az elso erteke legyen penzosszeg EURO-ban
a masodik erteke legyen, hogy 1 EURO hany forint

a harmadik valtozoban hatarozza meg, hogy az elso valtozoban
talalhato EURO mennyi forintnak felel meg, ezt tarolja el a
harmadik valtozoban, es jelenitse meg

pelda:

euro = 200
valtas = 380

kiirva: 76000

"""

euro = 200
valtas = 380

forint = euro * valtas

print( " a valtas eredmenye:")
print( forint )
