livro = {}
biblioteca =[]

while True:
    print('\n1 - Cadastrar novo livro'
        '\n2 - Consultar Livro'
        '\n3 - Adicionar informações'
        '\n4 - Remover informações'
        '\n5- Visualizar livros cadastrados'
        '\n6 - Sair')
    
    opcao = int(input('Informe a operação a ser realizada: '))
    
    match opcao:

        case 1:
            livro['TITULO'] = input('Informe o nome do livro: ').upper()
            livro['AUTOR'] = input(f'Informe o nome do autor do livro {livro['TITULO']}: ').upper()
            livro['ANO'] = int(input(f'Informe o ano do livro {livro['TITULO']}: '))
            livro['PAGINAS'] = int(input(f'Informe o numero de paginas que o {livro['TITULO']} contem: '))
            livro['DISPONIBILIDADE'] = input(f'Quantos exemplares do {livro['TITULO']} estao disponiveis: ').upper()
            print(f'\nO livro {livro['TITULO']} cadastrado!')
            biblioteca.append(livro.copy())
            livro.clear()

        case 2:
            procurando = input('Informe o livro que voce quer consultar: ').upper()
            for livro in biblioteca:
                if livro.get('TITULO') == procurando:
                    print(f'\n{livro}')
        
        case 3:
            procurando = input('Informe o livro que voce quer adicionar informações: ').upper()
            for livro in biblioteca:
                if livro.get('TITULO') == procurando:
                    nova_chave = input('Qual informação deseja adicionar? (Ex.: EDITORA, EDICAO, ETC)').upper()
                    novo_valor = input('O que voce quer adicionar nessa informação? ')
                    livro.update({nova_chave: novo_valor}) #livro[nova_chave] = novo_valor
                    print(f'\nInformação adicionada ao livro {livro["TITULO"]}!')

        case 4:
            procurando = input('Informe o livro que voce quer remover informações: ').upper()
            for livro in biblioteca:
                if livro.get('TITULO') == procurando:
                    chave_remover = input('Qual informação deseja remover? (Ex.: EDITORA, EDICAO, ETC)').upper()
                    if chave_remover in livro:
                        del livro[chave_remover]
                        print(f'\nInformação removida do livro {livro["TITULO"]}!')
                    else:
                        print(f'\nA informação {chave_remover} não existe no livro {livro["TITULO"]}.')

        case 5:
            if biblioteca:
                print('\nLivros cadastrados:')
                for livro in biblioteca:
                    print(livro)
            else:
                print('\nNenhum livro cadastrado.')

        case 6:
            print('\nPrograma encerrado.')
            break

        case _: 
            print('\nOpção inválida. Tente novamente.')




            
                
                
            
            
