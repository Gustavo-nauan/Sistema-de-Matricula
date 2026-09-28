import re

# obter o CPF do aluno e validar se é um CPF válido (11 dígitos)
def obter_cpf(mensagem="Digite o CPF do aluno (somente números): "):
    while True:
        cpf = input(mensagem)
        cpf_limpo = cpf.replace(".", "").replace("-", "")
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
            return cpf_limpo
        else:
            print(" ⚠️ CPF inválido. Por favor, digite um CPF válido (11 dígitos).")

# obter o RG do aluno e validar se é um RG válido (7 a 9 dígitos)
def obter_rg():
    while True:
        rg = input("Digite o RG do aluno (somente números ou terminados em X): ")
        rg_limpo = rg.replace(".", "").replace("-", "").strip().upper()
        if 7 <= len(rg_limpo) <=9:
            if rg_limpo.isdigit() or (rg_limpo[:-1].isdigit() and rg_limpo[-1] == "X"):
                return rg_limpo
            else:
                print(" ❌ ERRO: O RG deve conter apenas números ou terminar com 'X'.\n")
        else:
            print(" ⚠️ RG inválido. Por favor, digite um RG válido (7 a 9 digitos).")

# obter o telefone do aluno e validar se é um telefone válido (10 ou 11 dígitos)
def obter_telefone():
    while True:
        telefone = input("Digite o telefone com DDD (ex: 11999999999): ")
        telefone_limpo = telefone.replace("(","").replace(")", "").replace("-", "").replace(",", "").strip()
        if len(telefone_limpo) in [10,11] and telefone_limpo.isdigit():
            return telefone_limpo
        else:
            print(" ⚠️ Telefone inválido. por favor, digite um telefone com DDD e o número (10 ou 11 dígitos). ")

# obter o email do aluno e validar se é um email válido (contendo @ e .)
def obter_email():
        padrao_email = r'^[a-zA-z0-9_.=-]+@[a-zA-Z0-9-]+\.[a-zA-Z)-9-]+$'
        while True:
            email = input("Digite o email do aluno: ").strip()
            if re.match(padrao_email, email):
                return email
            else:
                print(" ⚠️ Email inválido. Por favor, digite um email válido (ex: nome@dominio.com)")
