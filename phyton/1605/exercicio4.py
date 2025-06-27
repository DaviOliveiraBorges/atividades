def ficha():
    nome = input("qual o nome do jogador? ")
    gols = input("quantos gols ele fez? ")

    if nome == "":
        nome = "desconhecido"

    if gols == "":
        gols = "0"

    print("Nome do jogador: ", nome)
    print("Numero de gols: ", gols)


ficha()