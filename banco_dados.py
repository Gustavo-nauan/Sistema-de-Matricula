import sqlite3
import logging 

# configuração do arquivo de auditoria;
logging.basicConfig(
    filename='sistema.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

def conectar():
    conexao = sqlite3.connect('teste.db')
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
        email TEXT NOT NULL UNIQUE,
        data_nascimento TEXT NOT NULL 
        );
    '''
    with conectar() as conexao:
        conexao.execute(sql)
   
def matricular_aluno(nome, curso, data_nascimento, cpf , rg, telefone, email):
    sql = '''
        INSERT INTO alunos(nome, curso, data_nascimento, CPF, RG, telefone, email) VALUES(?, ?, ?, ?, ? , ?, ?);'''
    valores = (nome, curso, data_nascimento, cpf, rg, telefone, email)

    try:
        with conectar() as conexao:
            conexao.execute(sql, valores)
            conexao.commit()
            logging.info(f"MATRÍCULA: Aluno '{nome}'(CPF: {cpf}) matriculado em '{curso}.")
            return True, f"\n ✅ Sucesso! O aluno {nome} foi matriculado."
    except sqlite3.IntegrityError as e:
        erro = str(e).lower()
        logging.warning(f"CONFLITO DE CADASTRO: Tentativa de duplicar dado (CPF: {cpf}, RG: {rg}, Email: {email}. Detalhes: {e})")
        if "cpf" in erro:
            return False, "\n❌ ERRO: Este CPF já está cadastrado no sistema."
        elif "rg" in erro:
            return False, "\n❌ ERRO: Este RG já está cadastrado no sistema."
        elif "email" in erro:
            return False, "\n❌ ERRO: Este Email já está cadastrado no sistema."
        else:
            return False, f"\n ❌ ERRO de integridade no banco de dados: {e}"
    except sqlite3.Error as e:
        logging.error(f"FALHA CRÍTICA DE BANCO na matrícula (CPF: {cpf}): {e}")
        return False, f"❌ERRO interno no banco de dados. Consulte o log do sistema."

def lista_alunos():
    sql = "SELECT * FROM alunos;"
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql)
        alunos_cadastrados = cursor.fetchall()
        return alunos_cadastrados
    
def lista_aluno_por_curso(termo_busca):
    slq = "SELECT * FROM alunos WHERE curso LIKE ?;"
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(slq, (f"%{termo_busca}%",))
        return cursor.fetchall()

def buscar_aluno_por_cpf(cpf):
    sql = "SELECT * FROM alunos WHERE CPF = ?;"
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (cpf,))
        return cursor.fetchone()
    finally:
        conexao.close()

def  remover_aluno_por_cpf(cpf):
    aluno = buscar_aluno_por_cpf(cpf)
    if aluno is None:
        logging.warning(f"REMOÇÂO FALHOU: Tentativa de remover CPF inexistente {cpf}")
        return False, f"⚠️ Nenhum aluno com o CPF: {cpf} foi encontrado pra remoção."
    sql = "DELETE FROM alunos WHERE CPF = ?;"
    conexao = conectar()
    try:
        conexao.cursor().execute(sql, (cpf,))
        conexao.commit()
        logging.info(f"ESCLUSÂO: Aluno: '{aluno['nome']}' (ID: {aluno['id']} | CPF: {cpf}) removido do banco de dados.")
        return True, f"\n✅ Aluno: {aluno['nome']} removido com sucesso."
    except sqlite3.Error as e:
        logging.error(f"FALHA CRITICA ao remover CPF {cpf}: {e}")
        return False, f"\n❌ ERRO interno ao tentar remover registro."
    finally:
        conexao.close()

def atualizar_curso(cpf, novo_curso):
    sql =  "UPDATE alunos SET curso = ? WHERE CPF = ?;"
    try:
        with conectar () as conexao:
            conexao.cursor().execute(sql, (novo_curso, cpf))
            conexao.commit()
            logging.info(f"UPDATE CURSO: CPF {cpf} alterado para '{novo_curso}'")
            return True, f"\n✅ Curso do aluno atualizados com sucesso."
    except sqlite3.Error as e:
        logging.error(f"FALHA DE UPDATE (curso) para CPF {cpf}: {e} ")
        return False, f"\n❌ ERRO ao tentar atualizar curso"
    
def atualizar_telefone(cpf, novo_telefone):
    sql =  "UPDATE alunos SET telefone = ? WHERE CPF = ?;"
    try:
        with conectar () as conexao:
            conexao.cursor().execute(sql, (novo_telefone, cpf))
            conexao.commit()
            logging.info(f"UPDATE TELEFONE: CPF {cpf} alterado para '{novo_telefone}'")
            return True, "\n✅ Telefone do aluno atualizados com sucesso."
    except sqlite3.Error as e:
        logging.error(f"FALHA DE UPDATE (telefone) para CPF {cpf}: {e}")
        return False, f"\n❌ ERRO ao tentar atualizar telefone"
    
def atualizar_email(cpf, novo_email):
    sql =  "UPDATE alunos SET email = ? WHERE email = ?;"
    try:
        with conectar () as conexao:
            conexao.cursor().execute(sql, (novo_email, cpf))
            conexao.commit()
            logging.info(f"UPDATE E-MAIL: CPF {cpf} alterado para '{novo_email}'.")
            return True, "\n✅ Email do aluno atualizados com sucesso."
    except sqlite3.IntegrityError:
        logging.warning(f"CONFLITO DE UPDATE: Tentativa de usar e-mail já existente ('{novo_email}') no CPF: {cpf}")
        return False, "\n❌ Este novo e_mail ja pertence a outro aluno"
    except sqlite3.Error as e:
        logging.error(f"FALHA DE UPDATE (E-mail) para o CPF {cpf}: {e}")
        return False, F"\n❌ ERRO ao tentar atualizar E-mail"
    
def contar_alunos_por_curso():
    sql = "SELECT curso, COUNT(*) as total FROM alunos GROUP BY curso;"
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    