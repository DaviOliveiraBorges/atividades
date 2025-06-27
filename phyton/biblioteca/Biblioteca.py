def AdicionarLivro(nome, ano):
    arquivo = open("livros.txt", "r")
    qtd = 0
    while True:
        linhas = arquivo.readline()
        qtd = qtd + 1
        if not linhas:
            break
    string = str(qtd)
    conteudo = string + "," + nome + "," + ano + "," + "disponivel" + "\n"
    with open("livros.txt", "a") as arquivo:
        arquivo.write(conteudo)
    arquivo.close()
    print("Livro adicionado com sucesso ")
    print("__" * 30)


def AdicionarAlunos(matricula, nome, email):
    arquivo = open("usuarios.txt", "r")
    if VerificaUsuario(matricula) == True:
        return False
    else:
        conteudo = matricula + "," + nome + "," + email + "," + "0" + "\n"
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(conteudo)
        arquivo.close()
        print("Aluno adicionado com sucesso ")
        print("__" * 30)


def VerificaUsuario(matricula):
    i = 0
    arquivo = open("usuarios.txt", "r")
    linhas = arquivo.readlines()

    while i < len(linhas):
        linha = linhas[i]
        partes = linha.strip().split(",")

        if matricula == partes[0]:
            print("Usuário existente")
            return True
        else:
            return False
    i += 1


def EmprestaLivro(matricula, NomeDoLivro):
    if VerificaUsuario(matricula) == True:
        i = 0
        with open("livros.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        with open("usuarios.txt", "r") as arquivo:
            linhas_User = arquivo.readlines()

        livro_encontrado = False

        while i < len(linhas):
            linha = linhas[i]
            partes = linha.strip().split(',')
            if len(partes) > 1:
                nome = partes[1]
                status = partes[3]

            if nome == NomeDoLivro:
                livro_encontrado = True
                if status == "disponivel":
                    partes[3] = "indisponivel"
                    linhas[i] = ",".join(partes) + "\n"
                    i = 0

                    while i < len(linhas_User):
                        linha_user = linhas_User[i]
                        partes = linha_user.strip().split(",")

                        if i < len(linhas_User):
                            historico = partes[3]
                            partes[3] = partes[3] + " - " + NomeDoLivro
                            linhas_User[i] = ",".join(partes) + "\n"

                        with open("usuarios.txt", "w") as arquivo:
                            arquivo.writelines(linhas_User)
                        i += 1

                    with open("livros.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

                    with open("emprestimos.txt", "a") as arquivo:
                        arquivo.write(matricula + "," + NomeDoLivro + "\n")
                        print("Livro emprestado com sucesso ")
                else:
                    print("Este livro está indisponível")
                    break
            i += 1

        if not livro_encontrado:
            print("Não temos este livro")
    else:
        print("Usuário não existe")


def RelatorioLivrosDispo():
    with open("livros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("livros_disponiveis.txt", "w") as relatorio:
        for linha in linhas:
            partes = linha.strip().split(",")
            if len(partes) > 3 and partes[3].strip() == "disponivel":
                relatorio.write(linha)

    print("Relatório de livros disponíveis gerado.")
    print("__" * 30)


def RelatorioLivrosEmp():
    with open("livros.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("livros_emprestados.txt", "w") as relatorio:
        for linha in linhas:
            partes = linha.strip().split(",")
            if len(partes) > 3 and partes[3].strip() == "indisponivel":
                relatorio.write(linha)

    print("Relatório de livros emprestados gerado.")
    print("__" * 30)


while True:
    acao = int(input("Digite sua ação \n" +
                     "1- Adicionar Livro: \n" +
                     "2- Adicionar Alunos: \n" +
                     "3- Empréstimo de livros: \n" +
                     "4- Gerar relatório de livros disponíveis: \n" +
                     "5- Gerar relatório de livros emprestados: \n" +
                     "6- Para Finalizar o programa: \n"
                     "--: "
                     ))

    if acao == 1:
        nome = input("Digite o nome do livro: ")
        ano = input("Digite o ano do livro: ")
        AdicionarLivro(nome, ano)
    elif acao == 2:
        matricula = input("Digite o matricula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        email = input("Digite o email do aluno: ")
        AdicionarAlunos(matricula, nome, email)
    elif acao == 3:
        nomeDolivro = input("Digite o nome do livro: ")
        matricula = input("Digite o matricula do aluno: ")
        EmprestaLivro(matricula, nomeDolivro)
    elif acao == 4:
        RelatorioLivrosDispo()
    elif acao == 5:
        RelatorioLivrosEmp()
    elif acao == 6:
        break
    else:
        print("Entrada inválida!")
