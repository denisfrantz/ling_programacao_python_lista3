class Carro:
    def __init__ (self):
        self._qtdLitros = 0
        self._kms = 0

    def abastecer (self, qtd):
        if qtd + self._qtdLitros > 50:
            self._qtdLitros = 50
        else:
            self._qtdLitros += qtd
    
    def mover (self, km):
        if km / 15 <= self._qtdLitros:
            self._kms += km
            self._qtdLitros -= km / 15

    def getLitros (self):
        return self._qtdLitros

    def getKms (self):
        return self._kms

carro1 = Carro()
carro2 = Carro()
carro1.abastecer(20)
carro2.abastecer(30)
carro1.mover(200)
carro2.mover(400)
print (f"Carro 1\nlitros em tanque: {round (carro1.getLitros(), 2)}\nKilometragem: {carro1.getKms()}")
print (f"Carro 2\nlitros em tanque: {round (carro2.getLitros(), 2)}\nKilometragem: {carro2.getKms()}")