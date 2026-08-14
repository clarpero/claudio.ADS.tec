estoque = []

def exibir_meu():
    print('\n:-:-:-:-:-: SISTEMA DE ESTOQUE :-:-:-:-:-:')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Pesquisar produto')
    print('4 - Atualizar produto')
    print('5 - Remover produto')
    print('6 - Encerrar programa')
pass

def cadastrar_produto(estoque):
    produto = {}
    produto['NOME'] = input('Informe o nome do produto: ')
    produtuo['PRECO'] = float(input('Informe o preço do produto: '))
    produto['QUANTIDADE'] = int(input('Informe a quantidade do produto em estoque: '))
    estoque.append(produto.copy)
    produto.clear()
    print('\nProduto cadastrado com sucesso!')
pass

def listar_produtos(estoque):
    if len(estoque) == 0:
        print('\nNenhum produto cadastrado!')
        
    print('\n:-:-: Produtos Cadastrados :-:-:')
    for produto in estoque:
        print(f'Nome: {produto['NOME']}')
        print(f'Nome: {produto['PRECO']:.2f}')
        print(f'Nome: {produto['QUANTIDADE']}')
        print('___')*10
pass

def pesquisar_produtos(estoque, nome):    
    for produto in estoque:
        if produto['NOME'].upper() == nome.upper():
            return produto
    return None

def atualizar_estoque(estoque, nome):
    produto = pesquisar_produtos(estoque, nome)
    if produto is None:
        print('Produto não encontrado!')
        return
    produto['QUANTIDADE'] = int(input('Atualize a quantidade do estoque: '))
pass

def remover_produto(estoque, nome):
    produto = pesquisar_produto(estoque, nome)
    if produto is None:
        print('Produto não encontrado!')
        return
    estoque.remove(produto)
    print('\nProduto removido com sucesso!')
pass

while True:
    exibir_meu()
    opcao = int(input('Informe o número da operação a ser realizada: '))
    
    match opcao:
        case 1:
            cadastrar_produto(estoque)
            
        case 2:
            listar_produtos(estoque)
            
        case 3:
            nome = input('Informe o nome do produto para procura: ')
            pesquisar_produto(estoque, nome)
            if produto:
                print('\nProduto encontrado!')
                print(f'\nProduto: {produto['NOME']}')
                print(f'\Preço: {produto['PRECO']}')
                print(f'\nQuantidade: {produto['QUANTIDADE']}')
            else:
                print('\nProduto não encontrado!')
        
        case 4:
            nome = input('Informe o nome do produto para procura: ')
            atualizar_estoque(estoque, nome)
        
        case 5:
            nome = input('Informe o nome do produto para procura: ')
            remover_produto(estoque, nome)
        
        case 6:
            print('Programa encerrado!')
            break
        
        case _:
            print('Opção inválida! Selecione uma opção entre 1 e 6')