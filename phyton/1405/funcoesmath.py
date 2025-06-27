from math import *

raio = float(input("qual o raio do circulo"))
print("area do raio: " , raio)
print("area: ", pi * pow(raio,2))
print("-" * 50)

n = int(input("forneça um valor inteiro "))
print("valor fornecido ", n)
print("raiz quadrada: ", sqrt(n))
print("-" * 50)

v1 = int(input("forneça o primeiro valor "))
v2 = int(input("forneça o segundo valor "))
if(v1 == v2):
    print("os valores sao iguais")
else:
    print("o menor valor é ", min(v1, v2))
    print("o meior valor é ", max(v1, v2))