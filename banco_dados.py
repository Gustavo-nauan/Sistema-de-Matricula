import sqlite3

# conexao com o banco de dados faculdade.db
def conectar():
    conexao = sqlite3.connect('faculdade.db')
    return conexao

# aql cria a tabela alunos no banco de dados faculdade.db
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
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
    cursor.execute(sql)
    conexao.commit()
    cursor.close()

# insere um novo aluno ao banco de dados faculdade.db
def matricular_aluno(nome, curso, idade, cpf , rg, telefone, email):
    sql = '''
        INSERT INTO alunos(nome, curso, idade, CPF, RG, telefone, email) VALUES(?, ?, ?, ?, ? , ?, ?);'''
    valores = (nome, curso, idade, cpf, rg, telefone, email)

    try:
        with conectar() as conexao:
            conexao.execute(sql,valores)

            return True, f"\n ✅Sucesso! O aluno {nome} foi matriculado."
    except sqlite3.IntegrityError:
        return False, f"\n Ja existe um aluno cadastrado com o CPF {cpf} ou RG {rg}." 
    

# aplica as máscaras apenas na exibição (dados continuam puros no SQLite)
def exibir_aluno(aluno):
    id_aluno = aluno[0]
    nome_aluno = aluno[1]
    curso_alunos = aluno[2]
    cpf_alunos = aluno[3]
    rg_alunos = aluno[4]
    telefone_alunos = aluno[5]
    email_alunos = aluno[6]
    idade_alunos = aluno[7]

    cpf_exibicao = f"{cpf_alunos[:3]}.{cpf_alunos[3:6]}.{cpf_alunos[6:9]}-{cpf_alunos[9:11]}"

    if len(rg_alunos) == 9:
        rg_exibicao = f"{rg_alunos[:2]}.{rg_alunos[2:5]}.{rg_alunos[5:8]}-{rg_alunos[8:9]}"
    else:
        rg_exibicao = rg_alunos

    if len(telefone_alunos) == 11:
        telefone_exibicao = f"({telefone_alunos[:2]}) {telefone_alunos[2:7]}-{telefone_alunos[7:11]}"
    else:
        telefone_exibicao = f"({telefone_alunos[:2]}) {telefone_alunos[2:6]}-{telefone_alunos[6:10]}"

    print(f" ID: {id_aluno} | nome: {nome_aluno} | curso: {curso_alunos}")
    print(f" CPF: {cpf_exibicao} | RG: {rg_exibicao} | idade: {idade_alunos}")
    print(f" telefone: {telefone_exibicao} | email: {email_alunos}")
    print("=" * 60)


# busca todos os alunos cadastrados no banco de dados faculdade.db
def lista_alunos():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = '''
        SELECT * FROM alunos;
    '''
    cursor.execute(sql)

    alunos_cadastrados = cursor.fetchall()
    conexao.close()

    if len(alunos_cadastrados) == 0:
        print("\n ⚠️ Nenhum aluno cadastrado no momento.")
        return

    print("===================== Alunos Cadastrados ====================")
    for aluno in alunos_cadastrados:
        exibir_aluno(aluno)


# busca um aluno específico pelo CPF (coluna UNIQUE)
def buscar_aluno_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM alunos WHERE CPF = ?;" , (cpf,))
    aluno = cursor.fetchone()
    conexao.close()

    return aluno
