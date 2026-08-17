# Crie um dicionário com nome, preço e estoque de um produto. Depois:
# - adicione a categoria;
# - atualize o preço;
# - aumente a quantidade em estoque;
# - apresente o dicionário atualizado.

dicionario = {}

dicionario['produto'] = input(f'Digite o nome do produto: ')
dicionario['preco'] = float(input(f'Informe o preço do {dicionario['produto']}: '))
dicionario['estoque'] = float(input(f'Informe o estoque do {dicionario['produto']}: '))

for chave,valor in dicionario.items():
    print([f'{chave} : {valor}'])


dicionario['categoria'] =  input(f'Qual a categoria do {dicionario['produto']}: ')
dicionario['preco'] = float(input(f'Qual o preço do {dicionario['produto']}: '))
dicionario['estoque'] = float(input(f'Qual o estoque do {dicionario['produto']}: '))

for chave,valor in dicionario.items():
    print([f'{chave} : {valor}'])