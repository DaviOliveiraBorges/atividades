palavra_antiga = "r"
palavra_nova = "o"

with open('exercicio7.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

conteudomodificado = conteudo.replace(palavra_antiga, palavra_nova)

with open('exercicio7(1).txt', 'w', encoding='utf-8') as f:
    f.write(conteudomodificado)
