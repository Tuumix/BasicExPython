class Robo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def posicionar(self, x, y):
        self.x = x
        self.y = y

    def posicao(self):
        print("Posicão de X : " + str(self.x) + " e Y : " + str(self.y))

robo = Robo(0,0)
robo.posicionar(2,3)
str = robo.posicao()




