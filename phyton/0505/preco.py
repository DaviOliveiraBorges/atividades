preco = float(input("Preço "))

print("1- pix/dinheiro 10% desconto")
print("2- Avista cartao 5% desconto")
print("3- Até 2x cartao normal")
print("4- Cartão 20% de júros")
escola = int(input())

if escola == 1:
    preco = preco * 0.9
    print("Preço atual: preço ", preco)
elif escola == 2:
    preco = preco * 0.95
    print("Preço atual: preço ", preco)
if escola == 3:
    print("Preço atual: preço ", preco)
if escola == 4:
    preco = preco * 1.2
    print("Preço atual: preço ", preco)