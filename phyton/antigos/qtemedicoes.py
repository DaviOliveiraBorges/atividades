tamanho = int(input("informe a quantidade de medições: "))
if tamanho > 0:
    total = 0
    for medicacao in range (tamanho):
        print("medicação nro. %2d" % (medicacao + 1))
        consumo = float(input("informe a medicacao de consumo "))