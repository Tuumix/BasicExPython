from random import randint

def verifica(sorteado, lista):
    cont = 0
    for obj in lista:
        for obj2 in sorteado:
            if obj == obj2:
                cont = cont + 1
    return cont

sorteado = []
lista = []

for cont in range(6):
    sorteado.append(randint(0,60))

for qtde in range(6):
    lista.append(int(input("Insira o número")))

print("Sua pontuação : " + str(verifica(sorteado,lista)))

