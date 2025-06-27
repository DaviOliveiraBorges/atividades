with open('exercicio5.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()
    for linha in linhas[1:4]:
        print(linha, end='')
