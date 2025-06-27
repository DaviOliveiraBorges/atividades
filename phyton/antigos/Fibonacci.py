Numero = int(input("Digite a quantidade de algarismos que voce quer: "))
n1 = int(input("digite o numero inicial da sequencia: "))
n2 = int(input("digite o segundo numero da sequencia: "))

sequencia = [n1, n2]
while len(sequencia) < Numero:
    sequencia.append(sequencia[-1] + sequencia[-2])
print(sequencia)
