while True:
    print("1: somar")
    print("2: multiplicar")
    print("3: maior")
    print("4: sovos Números")
    print("5: sair do Programa")

    opcao = int(input("escolha uma opção: "))

    if opcao == 5:
        print("saindo")
        break

    if opcao in [1, 2, 3, 4]:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))

    if opcao == 1:
        print("soma ", a + b)
    elif opcao == 2:
        print("multiplicacao", a * b)
    elif opcao == 3:
        if a > b:
            print("maior ", a)
        elif a < b:
            print("maior ", b)
        else:
            print("iguais")
    elif opcao == 4:
        continue
    else:
        print("Opção inválida.")