while True:
    nome = input("Fale seu nome: ")
    if len(nome) <= 3:
        print("Seu nome é menor que três caracteres. Digite outro nome.")
    else:
        break
while True:
    idade = int(input("Fale a sua idade: "))
    if idade >= 150:
        print("Você não tem mais que 150 anos, digite sua verdadeira idade.")
    else:
        break
while True:
    salario = float(input("Qual seu salário? "))
    if salario < 0:
        print("Seu salário não pode ser menor que zero.")
    else:
        break
sexo = input("Qual seu sexo? F ou M: ")
estCivil = input("Qual seu estado civil? S, C, V ou D? ")

print("Nome: ", nome, "Idade: ", idade, "Salário: ", salario, "Sexo: ", sexo, "Estado Civil: ", estCivil)
