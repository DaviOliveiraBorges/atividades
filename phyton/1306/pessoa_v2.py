class Pessoa:
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def mostrar(self):
        print("nome: ",self.nome)
        print("fone: ", self.fone)