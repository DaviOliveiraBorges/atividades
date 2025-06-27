with open('exercicio6.txt', 'r', encoding='utf-8') as f1, open('exercicio6 - Copia.txt', 'r', encoding='utf-8') as f2:
    conteudo1 = f1.read()
    conteudo2 = f2.read()

with open('resultadoexercicio6.txt', 'w', encoding='utf-8') as f3:
    f3.write(conteudo1 + "\n" + conteudo2)
