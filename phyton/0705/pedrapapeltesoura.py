from random import choice

choices_list = ['pedra', 'papel', 'tesoura']
escolhido = choice(choices_list)

print("""
COMPUTADOR: Vamos jogar pedra papel e tesoura
pedra ganha de tesoura
tesoura ganha de papel
papel ganha de pedra
""")

escolha = (input("qual voce escolhe? (pedra, papel, tesoura) \n"))

if escolha == escolhido:
    print("empate")
elif escolha == 'papel' and escolhido == 'pedra' or escolha == 'pedra' and escolhido == 'tesoura' or escolha == 'tesoura' and escolhido == 'pedra':
    print("voce ganhou")
else:
    print("voce perdeu")