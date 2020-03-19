class compra:
    def __init__(self, codigo, quantidade, valor):
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor

    def exibe(self):
        print(self.codigo)

lista = []
soma = 0

lista.append(comp(0, 1, 312))
lista.append(comp(1, 2, 12))
lista.append(comp(2, 2, 32))


for obj in lista:
    soma += obj.valor
    obj.exibe()

print(soma)
