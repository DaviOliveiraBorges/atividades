contatos = []
while True:
    nome = input("qual o nome do contato")
    if nome == " ": break
    contatos.append(nome)
for o in contatos:
    print(o)
