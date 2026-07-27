# Crie um menu com as opções: utilize match-case
# 1 - Novo cadastro
# 2 - Consultar cadastro
# 3 - Atualizar cadastro
# 4 - Remover cadastro

print('\n1 - Novo cadastro'
        '\n2 - Consultar cadastro'
        '\n3 - Atualizar cadastro'
        '\n4 - Remover cadastro')

opcao = int(input('Informe o numero da opção escolhida: '))

match  opcao:
    case 1 :
        print('Novo cadastro')
    case 2 :
        print('Consultar cadastro')
    case 3 :
        print('Atualizar cadastro')
    case 4 :
        print('Remover cadastro')
    case _ :
        print('Opção inválida')


