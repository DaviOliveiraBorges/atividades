valor = int(input("Digite o valor que deseja sacar: R$ "))

cedulas50 = valor // 50
valor %= 50
cedulas20 = valor // 20
valor %= 20
cedulas10 = valor // 10
valor %= 10
cedulas1 = valor // 1

print("cédulas fornecidas: ")
if cedulas50 > 0:
    print(cedulas50, "cedulas de R$50")
if cedulas20 > 0:
    print(cedulas20, " cedulas de R$20")
if cedulas10 > 0:
    print(cedulas10, " cedulas de R$10")
if cedulas1 > 0:
    print(cedulas1, " cedulas de R$1")