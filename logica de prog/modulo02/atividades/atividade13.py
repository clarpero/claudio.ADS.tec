# Crie um menu com as opções:
# 1 - Adicionar produto
# 2 - Remover produto
# 3 - Listar produtos
# 4 - Encerrar
# Os produtos deverão ser armazenados em uma lista durante a execução do programa.
lista = []

while True :
    print(
        f'\n1 - Adicionar produto'
        f'\n2 - Remover produto'
        f'\n3 - Listar produtos'
        f'\n4 - Encerrar')
    
    opcao = int(input('Informe a operação desejada: '))
    
    match opcao:
        case 1:
            produto = input('Informe o nome do produto: ').lower()
            lista.append(produto)
        case 2:
            print(lista)
            remover = input('Informe o produto para removar:').lower()
            lista.remove(remover)
        case 3:
            print(f'\nLista atual:\n{lista}')
        case 4:
            print('\nProgama encerrado!')
        case _ :
            print('\nOpção inválida!')