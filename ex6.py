class Elevador:
    def __init__(self, andares, capacidade):
        self._totalAndares = andares
        self._capacidade = capacidade
        self._andarAtual = 0
        self._qtdPessoas = 0

    def entra (self):
        if self._qtdPessoas < self._capacidade:
            self._qtdPessoas += 1

    def sai (self):
        if self._qtdPessoas > 0:
            self._qtdPessoas -= 1

    def sobe (self):
        if self._andarAtual < self._totalAndares:
            self._andarAtual += 1

    def desce (self):
        if self._andarAtual > 0:
            self._andarAtual -= 1

    def getAndares (self):
        return self._totalAndares

    def getAndarAtual (self):
        return self._andarAtual

    def getCapacidade (self):
        return self._capacidade

    def getPessoas (self):
        return self._qtdPessoas