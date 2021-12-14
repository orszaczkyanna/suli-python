# Osztály létrehozása

class Teglalap:
    # konstruktor neve mindig init 2 aláhúzásjellel határolva
    # minden osztálymetódusnak legalább 1 paramétere van, általában "self" elnevezéssel. A self magára az objektumra hivatkozik

    def __init__(self, a, b):  # inicializálás 
        self.hossz = a
        self.szelesseg = b

    # mivel ez egy osztálymetódus, legalább a self paramétert fel kell tüntetni
    def kerulet(self):
        return 2 * (self.hossz + self.szelesseg)

    def terulet(self):
        return self.hossz * self.szelesseg
    
    def kiir(self):  #kiírató metódus,, -kiir függvény-
        return "Hossz: " + str(self.hossz) + ", szélesség: " + str(self.szelesseg)



teglalap1 = Teglalap(3, 4)
teglalap2 = Teglalap(10, 20) #a "teglalap2" egy objektum

print("Az első téglalap kerülete:",teglalap1.kerulet())  #.kerulet metódus
print("A második téglalap kerülete:",teglalap2.kerulet())


print(teglalap1.kiir())  # .kiir metódus
print(teglalap2.kiir())

#  .lower --> metódus
#  .upper --> metódus

print("Az első téglalap területe: ", teglalap1.terulet())
print("A második téglalap területe: ", teglalap2.terulet())