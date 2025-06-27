from pessoa_v2 import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, fone, cargo):
        super().__init__(nome, fone)
        self.cargo = cargo

    def mostrar(self):
        super().mostrar()
        print(self.cargo)


f = Funcionario("Eli", "0000-0000", "Ator")
f.mostrar()
