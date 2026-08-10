# Crie um dicionário com informações de um livro e apresente separadamente:
# - todas as chaves;
# - todos os valores;
# - todos os pares chave-valor.

livro = {}

livro['Nome'] = input('Informe o nome do livro: ')
livro['Editora'] = input(f'Informe a editora do livro: {livro['Nome']}: ')
livro['Ano'] = int(input(f'Informe o ano do livro: {livro['Nome']}: '))
livro['Categoria'] = input(f'Informe o categoria do livro: {livro['Nome']}: ')

print('Chaves do Livro:')
print(livro.keys())

print('Valores do Livro:')
print(livro.values())

print('Chaves e Valores:')
print(livro.items())
