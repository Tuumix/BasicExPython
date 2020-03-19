class mergulhador:
    def __init__(self, id, nome, voltou):
        self.id = id
        self.nome = nome
        self.voltou = voltou

    def mergulhar(self):
        self.voltou = 0

    def voltar(self):
        self.voltou = 1

lista = []

lista.append(mergulhador(0, "Tanaka", 1))
lista.append(mergulhador(1, "Otsuka", 1))
lista.append(mergulhador(2, "Tsunoda", 1))
lista.append(mergulhador(3, "Kanazawa", 1))
lista.append(mergulhador(4, "Katoou", 1))

for obj in lista:
    obj.mergulhar()

while id != -1:
    id = int(input("ID do Mergulhador "))
    for obj in lista:
        if obj.id == id:
            obj.voltar()

print("MERGULHADORES QUE VOLTARAM")
for obj in lista:
    if obj.voltou == 0:
        print(str(obj.nome))