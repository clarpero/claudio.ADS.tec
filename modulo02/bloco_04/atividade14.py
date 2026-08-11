# Cadastre cinco produtos utilizando uma lista de dicionários. Para cada produto, 
# solicite ao usuário o nome, a categoria, o preço e a quantidade em estoque. 
# Ao final, percorra a lista e apresente todos os produtos cadastrados.
produtos = []
produto = {}



for i in range (5):
    print('\n:::::: Cadastro de produtos ::::::')
    produto['Nome'] = input(f'Informe o nome do produto {i+1}º: ')
    produto['Categoria'] = input('Informe a categoria do produto: ')
    produto['Preco'] = input('Informe o preco do produto: ')
    produto['Quantidade'] = input('Informe a quantidade em estoque do produto: ')
    produtos.append(produto.copy())
    produto.clear()

for produto in produtos:
    print('\n: : : Produto : : :')
    for chave,valor in produto.items():
        print(f'{chave} : {valor} ', end = '\n')