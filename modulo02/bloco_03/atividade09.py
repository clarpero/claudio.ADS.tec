# Crie um dicionário para armazenar:
# - nome;
# - idade;
# - cidade;
# - profissão.
# Apresente os dados utilizando as respectivas chaves.

# dados_pessoais = {
#     'nome' : input('Informe o seu nome: '),
#     'idade' : int(input('Informe a idade: ')),
#     'cidade' : input('Informe a cidade: '),
#     'profissao' : input('Informe a profissao: ')
# }

# print(dados_pessoais)

dados_pessoais = {}

dados_pessoais['nome'] = input('Informe o seu nome: ')
dados_pessoais['idade'] = int(input('Informe a idade: '))
dados_pessoais['cidade'] = input('Informe a cidade: ')
dados_pessoais['profissao'] = input('Informe a profissao: ')

print(dados_pessoais)