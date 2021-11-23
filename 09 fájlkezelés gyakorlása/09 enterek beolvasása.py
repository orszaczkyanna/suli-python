f = open("nevek.txt","r", encoding="utf8")

nevek = f.read() #egy nagy stringként olvassa be, amiben vannak enterek (\) is
f.close

nevlista = nevek.split("\n")
# ha for ciklussal olvasom be, akkor enterekig megy

for nev in nevek:
    print (nev,":", len(nev))