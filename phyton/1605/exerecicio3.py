def voto():
    idade = int(input("qual a sua idade? "))
    if idade <= 15:
        print("NEGADO")
    elif 16 <= idade < 18:
        print("OPCIONAL")
    else:
        print("OBRIGATÓRIO")

voto()