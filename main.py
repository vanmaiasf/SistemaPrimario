alunos={}
def listar_aluno():
    if len(alunos) > 0:
        print("Lista de alunos cadastrados: ")
        for matricula, dados in alunos.items():
            print(f"Matrícula: {matricula}")
            print(f"Nome: {dados['Nome']}")
            print(f"Telefone: {dados['Telefone']}")
    else:
        print("OPS Nenhum aluno cadastrado")

def cadastrar_aluno():
    matricula = input("Informe o número de matrícula do aluno: ")
    nome = input("Informe o nome do aluno: ")
    telefone = input("Informe o telefone do aluno: ")
    alunos[matricula] = {'Nome': nome, 'Telefone': telefone}
    print(f"Aluno {nome} cadastrado com sucesso!")

def editar_aluno():
    matricula = input("Informe o número de matrícula do aluno: ")
    if matricula in alunos:
        nome = input("Difite o nome do aluno")
        telefone = input("Digite o telefone do aluno")
        alunos[matricula] = {'Nome': nome, 'Telefone': telefone}
        print("Aluno editado com sucesso!")
    else:
        print("Aluno não encontrado")

def consultar_aluno():
    matricula = input("Informe o número de matrícula do aluno: ")
    if matricula in alunos:
        print(f"\nSegue os dados do ALUNO solicitado")
        print(f"\nMatrícula: {matricula}")
        print(f"\nAluno: {aluno}")
        print(f"\nTelefone: {telefone}")


while True:
    print("\nMenu:")
    print("1. Listar alunos")
    print("2. Cadastrar aluno")
    print("3. Excluir aluno")
    print("4. Consultar alunos")
    print("5. Editar aluno")
    print("6. Buscar aluno por nome")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_aluno()
    elif opcao == "2":
        cadastrar_aluno()
    elif opcao == "3":
        excluir_aluno()
    elif opcao == "4":
        consultar_aluno()
    elif opcao == "5":
        editar_aluno()
    elif opcao == "6":
        buscar_aluno()
    elif opcao == "0":
        print("Encerrando o programa")
        break
    else:
        print("Opção Inválida. Tente novamente.")