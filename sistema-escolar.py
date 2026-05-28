alunos_cadastrados = []
funcionarios_cadastrados = [ 
    {"Nome": "Ana azevedo", "Idade": "20 anos"},
    {"Nome": "Caio Aguiar", "Idade": "20 Anos"}, 
    {"Nome": "Lucia garcia", "Idade": "43 Anos"}
    ]

print("="*60)
print("BEM VINDO AO NEXUS ACADEMICO")
print("="*60)
print("Este sistema foi desenvolvido para gerenciar o fluxo de alunos e funcionarios " \
"da instituição de forma simples e rapida.")
print("FUNCIONALIDADES DISPONIVEIS:")
print("- Cadastrar e remover alunos da instituição.")
print("- Cadastrar e desligar funcionários do quadro ativo.")

def menu_de_opções ():
    print("="*60)
    print("NEXUS ACADEMICO")
    print("="*60)
    print("QUAL TIPO SERVIÇO IRA REALIZAR?")
    print("digite 1 para adicionar um aluno")
    print("digite 2 para removar um aluno")
    print("digite 3 para adicionar um funcionario")
    print("dgite 4 para remover um funcionario")
    print("digite 5 para ver os alunos cadastrados")
    print("digite 6 para ver os funcionarios cadastrados")
    print("digite 0 para encerrar o sistema")
    opcao_escolhida = int(input("Escolha uma opção: "))
    return opcao_escolhida

while True:
    opcao_escolhida = menu_de_opções()
    if opcao_escolhida == 1:

        enquanto_cadastrando = True

        while enquanto_cadastrando:

            nome_do_aluno = input("digite o nome completo do Aluno: ")
            idade_do_aluno = int(input("digite a idade do aluno: "))
            serie_do_aluno = input("digite qual serie o aluno esta atualmente: ")
            novo_aluno = {

            "Nome": nome_do_aluno,
            "idade": idade_do_aluno,
            "serie": serie_do_aluno,
            }
            alunos_cadastrados.append(novo_aluno)
            print("Aluno cadastrado com sucesso!")

            escolha = input("Deseja adicionar um novo aluno? (s/n): ")
            if escolha.lower() == 'n':
                print("voltando ao menu principal...")
                enquanto_cadastrando = False

    elif opcao_escolhida == 2:
        print("------- REMOVER ALUNO -------")

        nome_de_busca = input("digite o nome completo do aluno: ")

        aluno_encontrado = False

        for aluno in alunos_cadastrados:

            if aluno["Nome"].lower() == nome_de_busca.lower():
                alunos_cadastrados.remove(aluno)
                print(f"Aluno {aluno['Nome']} removido com sucesso!")
                aluno_encontrado = True
                break
        if not aluno_encontrado:
            print("Aluno nao encontrado no Sistema!")

    elif opcao_escolhida == 3:
        enquanto_cadastrando_funcionario = True

        while enquanto_cadastrando_funcionario:
            
            nome_do_funcionario_novo = input("Digite o nome do novo funcionario: ")
            idade_do_funcionario = int(input("Digite a idade do funcionario: "))
            novo_funcionario = {
                "Nome": nome_do_funcionario_novo,
                "Idade": idade_do_funcionario
            }
            funcionarios_cadastrados.append(novo_funcionario)
            print("Funcionario adicionado com Sucesso!")

            escolha_funcionario = input("Deseja adicionar um novo funcionario? (s/n): ")
            if escolha_funcionario.lower() == 'n':
                print("voltando ao menu principal...")
                enquanto_cadastrando_funcionario = False
    
    elif opcao_escolhida == 4:
        print("------- REMOVER FUNCIONARIO -------")
        nome_de_busca_de_funcionario = input("digite o nome completo do funcionario: ")

        funcionario_encontrado = False

        for funcionario in funcionarios_cadastrados:

            if funcionario["Nome"].lower() == nome_de_busca_de_funcionario.lower():
                funcionarios_cadastrados.remove(funcionario)
                print(f"funcionario{funcionario['Nome']} removido com sucesso!")
                funcionario_encontrado = True
                break
        if not funcionario_encontrado:
            print("Funcionario nao encontrado no Sistema!")

    elif opcao_escolhida == 5:
        if len(alunos_cadastrados) == 0:
            print("Nenhum aluno cadastrado no momento.")
        else:
            for aluno in alunos_cadastrados:
                print(f"Nome: {aluno['Nome']} | Idade: {aluno['idade']} | Série: {aluno['serie']}")

    elif opcao_escolhida == 6:
        if len(funcionarios_cadastrados) == 0:
            print("Nenhum funcionário cadastrado no momento.")
        else:
            for funcionario in funcionarios_cadastrados:
                print(f"Nome: {funcionario['Nome']} | Idade: {funcionario['Idade']}")

    elif opcao_escolhida == 0:
        print("Encerrando o programa... até mais!")
        break
    else:
        print("Erro! Digite uma opção valida!")