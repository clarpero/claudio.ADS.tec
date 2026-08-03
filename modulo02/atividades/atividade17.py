# Cadastre diversos produtos.
# O cadastro deverá continuar até que o usuário digite **fim**.
# Depois, solicite o nome de um produto e informe se ele está cadastrado.
# Caso exista, informe sua posição na lista.
lista_produtos = []
opcao = ''

while opcao != 'fim':
    produto = input('Informe o produto para cadastro: ').lower()
    if opcao == 'fim':
        print (f'Produtos cadastrados: {lista_produtos}')
    