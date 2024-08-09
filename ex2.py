class Pessoa:
    def __init__ (self, nome, idade, altura):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        
    def setNome (self, nome):
        self._nome = nome
        
    def setIdade (self, idade):
        self._idade = idade
        
    def setAltura (self, altura):
        self._altura = altura
        
    def getNome (self):
        return self._nome
    
    def getIdade (self):
        return self._idade
    
    def getAltura (self):
        return self._altura
    
    def mostraDados (self):
        print (f"Nome: {self._nome}\nIdade: {self._idade}\nAltura: {self._altura}")