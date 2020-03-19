from random import randint


class aluno:
    def __init__(self, id, nome, count):
        self.id = id
        self.nome = nome
        self.count = count

    def incrementa(self):
        if self.count > 3:
            print(self.nome + " Já foi sorteado 3 vezes!")
        else:
            self.count = self.count + 1


lista_aluno = []
i = 0

lista_aluno.append(aluno(0, "Jose", 0))
lista_aluno.append(aluno(1, "Maria", 0))
lista_aluno.append(aluno(2, "Tonhao", 0))

while (i < 10):
    lista_aluno[randint(0, 2)].incrementa()
    i = i + 1
