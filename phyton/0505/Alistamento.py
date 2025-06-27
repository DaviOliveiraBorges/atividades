from datetime import datetime
Nascimento = int(input("Digito o ano de nascimento: "))
AnoAtual = datetime.now().year
Idade = AnoAtual - Nascimento
if Idade < 18:
    print("Você ainda vai se alistar")
    Ano = 18 - Idade
    print("Sua idade é : ", Idade)
    print("Falta " , Ano, "Para você se alistar")
elif Idade == 18:
    print("Sua idade é : ", Idade)
    print("Está na hora de se alistar")
elif Idade > 18:
    print("Sua idade é : ", Idade)
    print("Passou da hora de se alistar")
    Ano = Idade - 18
    print("Passou" , Ano , "anos")



