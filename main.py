from validacoes import obter_cpf, obter_rg, obter_telefone, obter_email
from banco_dados import criar_tabela, matricular_aluno, lista_alunos, buscar_aluno_por_cpf


def menu():
    criar_tabela()
    while True:
        print("\n===================== Sistema de Cadastro de Alunos ====================")
        print("\n1 - Matricular Aluno")
        print("2 - Lista de Alunos")
        print("3 - Buscar Aluno por CPF")
        print("4 - Sair")

        opcao = input("\n Escolha uma opção (1, 2, 3 ou 4): ")

        if opcao == "1":
            nome = input("\nDigite o nome do aluno: ")
            curso = input("Digite o nome do curso: ")
            cpf = obter_cpf()
            rg = obter_rg()
            telefone = obter_telefone()
            email = obter_email()

            try:
                 idade = int(input("Digite a idade do aluno: "))
                 matricular_aluno(nome, curso, idade, cpf, rg, telefone, email)

            except ValueError:
                print("\n ⚠️ Erro: Por favor, digite uma idade válida (número inteiro).")

        elif opcao == "2":
            lista_alunos()

        elif opcao == "3":
            cpf = obter_cpf("Digite o CPF do aluno para busca (somente números): ")
            aluno = buscar_aluno_por_cpf(cpf)

            if aluno is None:
                print("\n ⚠️ Nenhum aluno encontrado com o CPF informado.")
            else:
                print("\n===================== Aluno Encontrado ====================")
                print(f" ID: {aluno[0]} | nome:{aluno[1]} | curso:{aluno[2]}")

        elif opcao == "4":
            print("\nSaindo do sistema...")
            break

        else:
            print("\n ⚠️ Opção inválida. por favor, escolha uma opção válida (1, 2, 3, 4) ")
if __name__ == "__main__":
    menu()