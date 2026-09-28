import sqlite3

def conectar():
    conexao = sqlite3.connect('faculdade.db')
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    sql = '''
        CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL,
        CPF TEXT NOT NULL UNIQUE,
        RG TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL,
        idade INTEGER 
        );
    '''
    with conectar() as conexao:
        conexao.execute(sql)
        
def matricular_aluno(nome, curso, idade, cpf , rg, telefone, email):
    sql = '''
        INSERT INTO alunos(nome, curso, idade, CPF, RG, telefone, email) VALUES(?, ?, ?, ?, ? , ?, ?);'''
    valores = (nome, curso, idade, cpf, rg, telefone, email)

    try:
        with conectar() as conexao:
            conexao.execute(sql, valores)
            return True, f"\n ✅ Sucesso! O aluno {nome} foi matriculado."
    except sqlite3.IntegrityError:
        return False, f"\n ❌ Erro: Já existe um aluno cadastrado com o CPF {cpf} ou RG {rg}." 

def lista_alunos():
    sql = "SELECT * FROM alunos;"
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql)
        alunos_cadastrados = cursor.fetchall()
        return alunos_cadastrados

def buscar_aluno_por_cpf(cpf):
    sql = "SELECT * FROM alunos WHERE CPF = ?;"
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql, (cpf,))
        aluno = cursor.fetchone()
        return aluno