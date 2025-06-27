def inprimir_cabecalho():
    print("*" * 30)
    print("*     Linguagem Phyton     *")
    print("*" * 30)

def contar(inicio, fim):
    for a in range(inicio, fim):
        print(a, end=" ")

def imprimir(texto):
    print(texto)

inprimir_cabecalho()
print()
imprimir("capitulo 7")
print()
contar(1, 10)