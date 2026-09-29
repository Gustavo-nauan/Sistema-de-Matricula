import banco_dados as bd
import validacoes as va


def menu():
    bd.criar_tabela()
    while True:
        print("\n===================== Sistema de Cadastro de Alunos ====================")
        print("\n1 - Matricular Aluno")
        print("2 - Lista de Alunos")
        print("3 - Buscar Aluno por CPF")
        print("4 - Remover aluno por CPF")
        print("5 - Atualizar dados do aluno")
        print("6 - Sair")

        opcao = input("\n Escolha uma opção (1, 2, 3, 4, 5 ou 6): ").strip()

        if opcao == "1":
            nome = input("\nDigite o nome do aluno: ").strip()
            curso = input("Digite o nome do curso: ").strip()
            cpf = va.obter_cpf()
            rg = va.obter_rg()
            telefone = va.obter_telefone()
            email = va.obter_email()

            while True:
                try:
                    idade = int(input("Digite a idade do aluno: "))
                    if 0 < idade < 120:
                        break
                    else:
                        print("❌ ERRO: Digite uma idade realista.")

                except ValueError:
                    print("\n ⚠️ Erro: Por favor, digite uma idade válida (número inteiro).")

            mensagem =  bd.matricular_aluno(nome, curso, idade, cpf, rg, telefone, email)
            print(mensagem)

        elif opcao == "2":
            alunos_cadastrados = bd.lista_alunos()
            if len(alunos_cadastrados) == 0:
                print("\n ⚠️ Nenhum aluno cadastrado.")
            else:
                print("\n===================== Alunos Cadastrados ====================")
                for alunos in alunos_cadastrados:
                    cpf_puro = alunos['CPF']
                    rg_puro = alunos['RG']
                    telefone_puro = alunos['telefone']

                    cpf_exibicao = f"{cpf_puro[:3]}.{cpf_puro[3:6]}.{cpf_puro[6:9]}-{cpf_puro[9:11]}"
                    if len(rg_puro) == 9:
                        rg_exibicao = f"{rg_puro[:2]}.{rg_puro[2:5]}.{rg_puro[5:8]}-{rg_puro[8:9]}"
                    else:
                        rg_exibicao = rg_puro
                    if len(telefone_puro) == 11:
                        telefone_exibicao = f"({telefone_puro[:2]}) {telefone_puro[2:7]}-{telefone_puro[7:11]}" 
                    else:
                        telefone_exibicao = f"({telefone_puro[:2]}) {telefone_puro[2:6]}-{telefone_puro[6:10]}"
                        
                    print(f" ID: {alunos['id']} | Nome: {alunos['nome']} | Curso: {alunos['curso']}")
                    print(f" CPF: {cpf_exibicao} | RG: {rg_exibicao} | Idade: {alunos['idade']}")
                    print(f" Telefone: {telefone_exibicao} | E-mail: {alunos['email']}")
                    print("=" * 60)

        elif opcao == "3":
            cpf = va.obter_cpf("Digite o CPF do aluno para busca (somente números): ")
            aluno = bd.buscar_aluno_por_cpf(cpf)

            if aluno is None:
                print("\n ⚠️ Nenhum aluno encontrado com o CPF informado.")
            else:
                print("\n===================== Aluno Encontrado ====================")
                print(f" ID: {aluno['id']} | Nome: {aluno['nome']} | Curso: {aluno['curso']}")

        elif opcao == "4":

            cpf = va.obter_cpf("Digite o CPF do aluno que deseja remover: ")
            sucesso, mensagem = bd.remover_aluno_por_cpf(cpf)
            print(mensagem)

        elif opcao == '5':
            cpf = va.obter_cpf("Digite o CPF do aluno que deseja fazer as alterações: ")
            aluno_existente = bd.buscar_aluno_por_cpf(cpf)
            if aluno_existente is None:
                print("\n⚠️ ERRO: Nenhum aluno encontrado com esse CPF.")
            else:
                while True:
                    print(f"\n===================== Atualizar Dados: {aluno_existente['nome']} ====================")
                    print("1 - Alterar Curso")
                    print("2 - Alterar Telefone")
                    print("3 - Altera Email")
                    print("4 - Concluir e voltar ao Menu principal")

                    sua_opcao = input("Digite oque você deseja alterar (1 a 4): ").strip()
                    if sua_opcao == '1':
                        novo_curso = input("Digite o novo curso: ")
                        sucesso, mensagem = bd.atualizar_curso(cpf, novo_curso)
                        print(mensagem)

                    elif sua_opcao == '2':
                        novo_telefone = input("Digite o novo telefone: ")
                        sucesso, mensagem = bd.atualizar_telefone(cpf, novo_telefone)
                        print(mensagem)

                    elif sua_opcao == '3':
                        novo_email = input("Digite o novo email: ")
                        sucesso, mensagem = bd.atualizar_email(cpf, novo_email)
                        print(mensagem)

                    elif sua_opcao == '4':
                        print("Voltando para o menu principal.")
                        break
                    else:
                        print("Digite uma opção válida. Escolha de 1 a 4")

        elif opcao == "6":
            print("\nA sair do sistema...")
            break

        else:
            print("\n ⚠️ Opção inválida. Por favor, escolha uma opção válida (1, 2, 3, 4) ")

if __name__ == "__main__":
    menu()