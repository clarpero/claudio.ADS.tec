# Desenvolva um programa que simule o cadastro simplificado de livros de uma biblioteca.
# O sistema deverá apresentar um menu com as seguintes opções:
# 1 - Cadastrar livro
# 2 - Listar livros
# 3 - Pesquisar livro
# 4 - Remover livro
# 5 - Encerrar
# Os livros deverão ser armazenados em uma lista durante toda a execução do programa.
# Ao pesquisar ou remover um livro inexistente, o sistema deverá informar o usuário.
lista_de_livros = []

while True:
    
    print(
        f'\n1 - Cadastrar livro'
        f'\n2 - Listar livros'
        f'\n3 - Pesquisar livro'
        f'\n4 - Remover livro'
        f'\n5 - Encerrar')
    
    opcao = input('Informe a opção desejada: ')
    if opcao.isdecimal() == True:
        opcao = int(opcao)
    else:
        print('\nOpção inválida! Informe apenas números.')
        continue
          
    match opcao:
        case 1:
            livro = input('Informe o nome do livro: ').lower()
            lista_de_livros.append(livro)
        
        case 2:
            print(f'\nAqui está a lista de todos os livros cadastrados:'
                f'{lista_de_livros}')
            
        case 3:
            livro = input('\nInforme o nome do livro para pesquisa: ').lower()
            lista_de_livros.count(livro)
            if lista_de_livros.count(livro) == 0:
                print(f'\nO livro informado {livro} não foi encontrado.')
            else:
                print(f'\nO livro informado {livro} foi encontrado.')
        
        case 4:
            livro = input('\nInforme o nome do livro para remover: ').lower()
            if livro in lista_de_livros :
                print(f'\nO livro informado {livro} foi removido.')
                lista_de_livros.remove(livro)
            else:
                print(f'\nO livro informado {livro} não foi encontrado.')
        
        case 5:
            print("\nPrograma encerrado!")
            break
        
        case _:
            print('Opção inválida!')
