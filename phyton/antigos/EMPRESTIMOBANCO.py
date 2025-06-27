preco = float(input("qaul o valor da casa? \n"))
sal = float(input("qual o seu salario? \n"))
tempo = int(input("em quantos anos voce vai pagar? "))

mensalidade = preco/(tempo * 12)
print("valor da casa ", preco)
print("pestacao ", mensalidade)

if mensalidade >= (sal * 30/100):
    print("salario excedeu, nao compre")
else:
    print("pode compra")

