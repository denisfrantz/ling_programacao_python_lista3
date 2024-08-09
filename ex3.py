class Pessoa:
    def __init__ (self):
        self._nome = None
        self._idade = None
        self._altura = None

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

    def mostraDados(self):
        print(f"Nome: {self._nome}\nIdade: {self._idade}\nAltura: {self._altura}")

class Agenda:
    def __init__ (self):
        self.povo = []

    def armazenaPessoa (self, nome, idade, altura):
        p = Pessoa()
        p.setNome(nome)
        p.setIdade(idade)
        p.setAltura(altura)
        self.povo.append(p)

    def buscaPessoa (self, nome):
        i = 1
        for p in self.povo:
            if p.getNome() == nome:
                return i
            else:
                i += 1
        return 0

    def imprimePessoa (self, posicao):
        if posicao != 0:
            p = self.povo[posicao-1]
            p.mostraDados()

    def imprimePovo (self):
        for p in self.povo:
            self.imprimePessoa(self.buscaPessoa(p.getNome()))