import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTERGER PRIMARY KEY,
    nome TEXT NOT NULL, 
    cargo TEXT
    )
''')

cursor.execute('INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)',('Ana', 'desenvolvedora'))
cursor.execute('INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)',('Marco', 'ladrão'))XX
cursor.execute('INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)',('Joao', 'bombeiro'))
conexao.commit()
for linha in cursor.execute("SELECT nome, cargo FROM funcionarios"):
    print(f"Funcionario: {linha[0]}, Cargo: {linha[1]}")
conexao.close()