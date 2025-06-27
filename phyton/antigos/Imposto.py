# -*- coding: utf-8 -*-

salario = float(input("Digite o salário: "))

if(salario < 1903.98):
    print("Isento ")
elif(salario < 2826.65):
    imposto = 7.5/100*salario
    salario = salario * 0.925
    print("Seu salário após o desconto é: ", salario, "imposto de: " , imposto)
elif(salario < 3751.05):
    imposto = 15/100*salario
    salario = salario * 0.85

    print("Seu salário após o desconto é: ", salario, "imposto de: " , imposto)
elif(salario < 4664.68):
    imposto = 22.5/100*salario
    salario = salario * 0.775
    print("Seu salário após o desconto é: ", salario, "imposto de: " , imposto)
else:
    imposto = 27.5/100*salario
    salario = salario * 0.725

    print("Seu salário após o desconto é: ", salario, "imposto de: " , imposto)




