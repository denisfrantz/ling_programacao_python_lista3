class ControleCanal:
    def aumentaCanal (self, tv):
        if tv.canal == 99:
            tv.canal = 1
        else:
            tv.canal += 1
        
    def diminuiCanal (self, tv):
        if tv.canal == 1:
            tv.canal = 99
        else:
            tv.canal -= 1

    def selecionaCanal (self, tv, canal):
        if canal == 0 or canal > 99:
            tv.canal = 1
        else:
            tv.canal = canal

class ControleSom:
    def aumentaVol (self, tv):
        if tv.volume < 100:
            tv.volume += 1
        
    def diminuiVol (self, tv):
        if tv.volume > 0:
            tv.volume -= 1

class Televisao:
    def __init__ (self):
        self.volume = 10
        self.canal = 1
        self.controleVolume = ControleSom()
        self.controleCanal = ControleCanal()

    def getVolume (self):
        return self.volume

    def getCanal (self):
        return self.canal

tv = Televisao()
controleSom = tv.controleVolume
controleCanal = tv.controleCanal
controleSom.aumentaVol(tv)
controleSom.aumentaVol(tv)
controleSom.diminuiVol(tv)
controleCanal.aumentaCanal(tv)
controleCanal.aumentaCanal(tv)
controleCanal.diminuiCanal(tv)

print(f"Canal: {tv.getCanal()}")
print(f"Volume: {tv.getVolume()}")

controleCanal.selecionaCanal(tv, int(input("Selecione um canal: ")))

print(f"Canal: {tv.getCanal()}")
print(f"Volume: {tv.getVolume()}")