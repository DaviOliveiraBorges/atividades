altura = float(input("Digite a altura "))
peso = float(input("Digite o peso "))

total = peso // (altura**2)
print(total)

if total < 18.5:
    print("Abaixo do peso")
elif total >= 18.5 and total < 25:
    print("peso ideal")
elif total >= 25 and total < 30:
    print("Sobrepeso")
elif total >= 30 and total < 40:
    print("obesidade")
else:
    print("Obesidade mórbida")