Idade = int(input("Digite a idade do nadador: "))

if Idade <= 9:
    print("Nadador mirim")
elif Idade <= 14:
    print("Infantil")
elif Idade <= 19:
    print("júnior")
elif Idade <= 20:
    print("Sênior")
else:
    print("Master")
