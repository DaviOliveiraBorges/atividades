palavra = input("qual a sua palavra? ")

tamanho = len(palavra)


def escreva():
    print("~" * tamanho)
    print(palavra)
    print("~" * tamanho)

escreva()