from random import randint

ran = randint(0, 5)
tentativas = 0
acertou = False

print("Estou pensando em um número entre 0 e 5 ")
print(ran)

while acertou == False:
    num = int(input("Em qual número pensei? "))
    tentativas += 1

    if num == ran:
        acertou = True
        print("Você acertou em", tentativas, " tentativas")
    else:
        print("Você errou. Tente novamente.")
        if num > ran:
            print("maior")
        else:
            print("menor")