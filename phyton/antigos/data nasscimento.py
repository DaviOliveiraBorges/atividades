from datetime import date

nasc = int(input("em qual ano voce nasceu? \n"))
ano_atual = datetime.now().year
print("ano atual: {}".format(ano_atual))
idade = (ano_atual - nasc)
    print
