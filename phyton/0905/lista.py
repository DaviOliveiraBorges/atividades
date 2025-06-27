sudeste = ['SP', 'MG', 'RJ', 'ES']
notas = [5.4, 7.5, 8.6, 10]
qtde_estados_sudeste = len(sudeste)

print("estados sudeste")
for n in range(qtde_estados_sudeste):
    print(n + 1, sudeste[n])
print('-' * 30)

print("notas")
for n in notas:
    print(n)
