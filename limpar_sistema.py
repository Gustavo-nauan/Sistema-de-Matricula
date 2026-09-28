import sqlite3

conexao = sqlite3.connect('faculdade.db')
cursor = conexao.cursor()

cursor.execute("DELETE FROM alunos;")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='alunos';")

conexao.commit()
conexao.close()

print("\n ✅ Sucesso! Todos os alunos foram removidos do banco de dados da faculdade.db. ")