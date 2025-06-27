m = float(input("digite seu peso (em kg): \n"))
h = float(input("digite sua altura (em m): \n"))

imc = (m / (h ** 2))

if imc < 18.5:
    print("abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("peso ideal")

elif imc > 25 and imc <= 30:
    print("obesidade")

elif imc > 30:
    print("obesiadade morbida")