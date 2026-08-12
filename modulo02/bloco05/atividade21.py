# Solicite ao usuário o nome, o preço e a quantidade em estoque de um produto. 
# Crie uma função que receba esses dados como parâmetros e retorne um dicionário representando o produto. 
# Ao final, apresente o cadastro criado.
def cadastrando_produto():
    produto ={}
    produto['NOME'] = input('Informe o nome do produto: ')
    produto['PRECO'] = float(input('Informe o preco do produto: '))
    produto['QUANTIDADE'] = int(input('Informe a quantidade do produto em estoque: '))
    return produto

produto = cadastrando_produto().copy()

print(produto)
