# Cadastre vários produtos em uma lista de dicionários, armazenando nome, preço e quantidade em estoque. 
# Em seguida, solicite ao usuário o nome de um produto, localize o registro correspondente e permita atualizar sua quantidade em estoque. 
# Caso o produto não seja encontrado, informe ao usuário. Ao final, apresente os dados atualizados.
produtos = [
            {'NOME' : 'ARROZ',
            'PRECO' : 11.99,
            'QUANTIDADE' : 30},
            
            {'NOME' : 'FEIJAO',
            'PRECO' : 6.99,
            'QUANTIDADE' : 14},
            
            {'NOME' : 'MACARRAO',
            'PRECO' : 9.99,
            'QUANTIDADE' : 32},
            
            {'NOME' : 'LEITE',
            'PRECO' : 7.99,
            'QUANTIDADE' : 26},
]

procura = input('Informe o nome do produto para procurar: ').upper()

while True:
    for produto in produtos:
        if produto.get('NOME') == procura:
            print('\nProduto encontrado!\n')
            for chave, valor in produto.items():
                print(f'{chave} : {valor}')
            print(end='\n')
        produto['QUANTIDADE'] = int(input('Informe o novo estoque do item: '))
        print(produto)
        break
    else:
        print('Produto não encontrado!')
    break

