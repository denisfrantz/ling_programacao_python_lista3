class Circulo:
    PI = 3.14
    def __init__ (self, raio, x, y):
        self.x_centro = x
        self.y_centro = y
        self.raio = raio
        self.__area = None
        self.__circunferencia = None
        self.__calculaArea(raio)
        self.__calculaCircunferencia(raio)
    
    def __calculaArea (self, raio):
        self.__area = self.PI * (raio * raio)

    def __calculaCircunferencia (self, raio):
        self.__circunferencia = 2 * self.PI * raio
    
    def setRaio (self, raio):
        self.raio = raio
        self.__calculaArea(raio)
        self.__calculaCircunferencia(raio)

    def aumentaRaio (self, percentual):
        self.raio += self.raio * percentual / 100
        self.__calculaArea(self.raio)
        self.__calculaCircunferencia(self.raio)

    def setCentro (self, x, y):
        self.x_centro = x
        self.y_centro = y

    def getRaio (self):
        return self.raio

    def printCentro (self):
        print(f"( {self.x_centro}, {self.y_centro} )\n")

    def getArea (self):
        return self.__area

    def getCircunferencia (self):
        return self.__circunferencia

raio = float(input("Insira valor do raio: "))
x = int(input("Insira posição do centro (X e Y):\n"))
y = int(input())
c = Circulo(raio, x, y)
c.printCentro()
print(f"Raio: {c.getRaio()}\nArea: {c.getArea()}\nCircunferência: {c.getCircunferencia()}")
print("Insira nova posição do centro (X e Y): ")
c.setCentro(int(input()), int(input()))
c.setRaio(int(input("Insira novo raio: ")))
c.printCentro()
print(f"Raio: {c.getRaio()}\nArea: {c.getArea()}\nCircunferência: {c.getCircunferencia()}")
c.aumentaRaio(float(input("Insira aumento percentual do raio: ")))
c.printCentro()
print(f"Raio: {c.getRaio()}\nArea: {c.getArea()}\nCircunferência: {c.getCircunferencia()}")
