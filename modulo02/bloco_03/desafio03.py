livro = {}
biblioteca =[]

while True:
    print('\n1 - Cadastrar novo livro'
        '\n2 - Consultar Livro'
        '\n3 - Adicionar informações'
        '\n4 - Remover informações'
        '\n5- Visualizar livros cadastrados')
    
    opcao = int(input('Informe a operação a ser realizada: '))
    
    match opcao:
        case 1:
            livro['TITULO'] = input('Informe o nome do livro: ').upper()
            livro['AUTOR'] = input(f'Informe o nome do autor do livro {livro['TITULO']}: ').upper()
            livro['ANO'] = int(input(f'Informe o ano do livro {livro['TITULO']}: '))
            livro['PAGINAS'] = int(input(f'Informe o numero de paginas que o {livro['TITULO']} contem: '))
            livro['DISPONIBILIDADE'] = input(f'Informe se existe exemplares do {livro['TITULO']} disponiveis: ').upper()
            print(f'\nO livro {livro['TITULO']} cadastrado!')
            biblioteca.append[livro]
            livro.clear()
        case 2:
            procurando = input('Informe o livro que voce quer consultar: ').upper()
            if procurando == biblioteca[livro.get(procurando)]:
                print(biblioteca[livro])
        
        case 3:
            procurando = input('Informe o livro que voce quer adicionar informações: ').upper()
            if procurando == biblioteca[livro.get(procurando)]:
                for chave, valor in biblioteca[livro.items]:
                    print(biblioteca[livro[chave]], biblioteca[livro[valor]])
            atualizar = input('Qual informação deseja adicionar: ').upper()
            biblioteca[livro.update(atualizar)]
                
            
                
                
            
            

