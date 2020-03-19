from random import randint

lista1 = []
lista2 = []
lista3 = []

for tam in range(10):
    lista1.append(randint(0,10))
    lista2.append(randint(0,10))
    lista3.append(lista1[tam] + lista2[tam])

print(lista1)
print(lista2)
print(lista3)