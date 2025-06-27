class Item:
    def __init__(self, produto, qtde, preco):
        self.produto = produto
        self.qtde = qtde
        self.preco = preco

    def mostrar(self):
        print(self.produto, " - ", self.qtde, " - ", self.preco)


class Pedido:
    def __init__(self, numero, data):
        self.numero = numero
        self.data = data
        self.item1 = Item("Caneta", 10, 1.53)
        self.item2 = Item("Lápis", 5, 0.35)
        self.total = self.item1.qtde * self.item1.preco + \
                     self.item2.qtde * self.item2.preco

    def mostrar(self):
        print("Numero ", self.numero)
        print("Data ", self.data)
        print("-" * 20)
        self.item1.mostrar()
        self.item2.mostrar()
        print("-" * 20)
        print("Total ", self.total)


p = Pedido(1, "10/4/2020")
p.mostrar()
