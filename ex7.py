class Relogio:
    def __init__ (self):
        self._hora = 0
        self._minuto = 0
        self._segundo = 0

    def setHora (self, hora, minuto, segundo):
        if hora < 24 and minuto < 60 and segundo < 60:
            self._hora = hora
            self._minuto = minuto
            self._segundo = segundo

    def getHora (self):
        print (f"Horário atual: {self._hora}h {self._minuto}min {self._segundo}seg")

    def avancaHorario (self):
        if self._segundo == 59:
            self._segundo = 0
            
            if self._minuto == 59:
                self._minuto = 0
                
                if self._hora == 23:
                    self._hora = 0
                else:
                    self._hora += 1
                    
            else:
                self._minuto += 1
                
        else:
            self._segundo += 1