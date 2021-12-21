# DICTIONARY

szotar = {"palyesz" : 175, "szekreny" : 2, "ablak" : 1.5}

# üreset is lehet létrehozni 
# egy kulcshoz csak egy érték tartozhat

# kulcs : érték
# pajesz kulcs értéke 175
# elemek vesszővel elválasztva



# a kulcson keresztül hozzáférek az értékhez (hasonló, mint az index)
print(szotar["palyesz"])
print(szotar["szekreny"])
print(szotar["ablak"])
# ha nincs valamilyen elem, akkor hibát ad

# hozzáfűzés:
szotar.update( {"eger" : 22, "cica" : 33} )
print(szotar["cica"])

# közvetlenül tudok értéket módosítani
szotar["palyesz"] = 123
print(szotar["palyesz"])


# meg tudom vizsgálni, hogy létezik-e egy adott kulcs
# .key  () - összes kulcs lekérése
if "cica" in szotar.keys():
    print("benne van a szótárban a kulcs")
else:
    print ("nincs benne a szótárban a kulcs")

# szotar.values()
# .values() segítségével a szótárban szereplő értékeket tudom lekérdezni