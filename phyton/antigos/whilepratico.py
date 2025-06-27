total = 0
itens = 0
preco = 1

print("digite o preco dos produtos ou 0 pra caba")
while preco != 0:
    preco = float(input("preço? "))
    if preco != 0:
        total += preco
        itens += 1
print("-" * 35)
print("qte de itens", itens)
print("valor total", total)
print("-" * 35)
print("pro")