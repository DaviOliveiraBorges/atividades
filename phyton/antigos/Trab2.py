import random

vitorias = 0
while True:
    jogador = int(input("Escolha um número: "))
    escolha = input("Par ou Ímpar? (p/i): ").lower()
    computador = random.randint(0, 10)
    total = jogador + computador

    print("Você jogou ", jogador, " e o computador ", computador, "Total: ", total)

    if (total % 2 == 0 and escolha == 'p') or (total % 2 == 1 and escolha == 'i'):
        vitorias += 1
        print("ganhou")
    else:
        print("perdeu. Total de vitórias: ", vitorias)
        break
