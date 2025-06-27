def notas():

    qte_notas = int(input("informe a quantidade de notas: "))
    total_notas = 0
    maior_nota = 0
    menor_nota = 100
    if qte_notas > 0:
        total = 0
        for i in range (qte_notas):
            print("nota nro. %2d" % (i + 1))
            nota_aluno = float(input("informe a nota "))
            total_notas = total_notas + nota_aluno
            if nota_aluno > maior_nota:
                maior_nota = nota_aluno
            if nota_aluno < menor_nota:
                menor_nota = nota_aluno

    print("QUANTIDADE DE NOTAS: ", qte_notas)
    print("MAIOR NOTA: ", maior_nota)
    print("MENOR NOTA: ", menor_nota)
    media_turma = total_notas / qte_notas
    print("MÉDIA DA TURMA", media_turma)