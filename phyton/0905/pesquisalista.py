lista = ['maionese', 'ervilha', 'carne','tomate']
produto = input("nome do produto")
if produto in lista:
    print("produto jaw existente")
else:
    lista.append(produto)
    print("produto adicionado")
print("lista atual de produtos")
for p in lista:
    print(p)