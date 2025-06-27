soma = 0
lista_precos = []
print("informe os precos do produto")
for cont in range(10):
    mensagem = "produto" + str(cont+1) + ": "
    preco = float(input(mensagem))
    soma += preco
    lista_precos.append(preco)
media = soma/10
print("o preco medio é", media)
print("os precos acima da media sao: ")
for cont in range(10):
    if lista_precos[cont] > media:
        print("produto", cont + 1)
        print("preço ", lista_precos[cont])