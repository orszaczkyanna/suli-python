# Házi feladat: megkeresni a legkisebb elemet és annak a helyét


lista = [1,5,7,26,-4,3,88,12,]

legkisebb = lista[0]
minindex = 0

for i in lista:
    if i < legkisebb:
        legkisebb = i

print ("A legkisebb elem:",legkisebb)

for i in range (0,len(lista)):
    if lista[i] < lista[minindex]:
        minindex = i

print ("A legkisebb elem helye:", minindex)





# lista legnagyobb elemének a helye
lista = [3,6,25,8,25,22,12]

maxindex = 0
for i in range (0, len(lista)):
    if lista [i] > lista [maxindex]:
        maxindex = i

print ("A lista legnagyobb elemének (első)helye:", maxindex)
