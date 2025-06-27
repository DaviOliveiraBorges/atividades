lista_compras = []
while True:
    escolha_usuario = input("""
    O que voce deseja fazer?

    digite 1 para adicionar contato
    digite 2 para remover um contato
    digite 3 para mostrar seus itens
    digite 4 para mostrar se o produto ja esta na lista
    digite 5 para sair do programa
    """)
    print("-" * 80)



    if escolha_usuario == '1':
        while True:
            nome = input("Qual o nome do produto? ")
            if nome == "":
                print("-" * 80)
                break
            lista_compras.append(nome)
        for a in lista_compras:
            print(a)
    elif escolha_usuario == '2':
        excluir = input("Qual produto deseja excluir? ")
        if excluir in lista_compras:
            lista_compras.remove(excluir)
            for a in lista_compras:
                print(a)
        else:
            print("produto não encontrado.")
    elif escolha_usuario == '3':
        if lista_compras:
            print("Seus itens:")
            for a in lista_compras:
                print(a)
        else:
            print("Nenhum contato salvo.")
    elif escolha_usuario == '4':
        produto = input("nome do produto")
        if produto in lista_compras:
            print("produto ja existente")
        else:
            print("produto ainda nao esta na lista")
        for a in lista_compras:
            print(a)
    elif escolha_usuario == "5":
        print("Saindo")
        break
    else:
        print("Opção inválida")
