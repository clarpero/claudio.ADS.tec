# Solicite ao usuário o nome, o e-mail e a cidade de uma pessoa e armazene essas informações em um dicionário. 
# Em seguida, solicite o nome de uma chave e utilize get() para consultar o valor correspondente. 
# Caso a chave não exista, informe que o dado não foi encontrado.

dados = {}

dados['nome'] = input('Informe o nome: ')
dados['email'] = input('Informe o email: ')

print(dados)

chave = input('Informe a chave para procura: ')
print(f'{dados.get(chave, 'Chave não cadastrada.')}')   #dicionario.get( PROCURA, 'Texto para imprimir')
