# Cadastre diversos produtos.
# O cadastro deverá continuar até que o usuário digite **fim**.
# Depois, solicite o nome de um produto e informe se ele está cadastrado.
# Caso exista, informe sua posição na lista.
lista_produtos = []
produto = ''

while produto != 'fim':
    produto = input('Informe o produto para cadastro ou digite FIM para sair: ').lower()
    if produto == 'fim':
        checagem = input('Informe o nome do produto para conferir: ').lower()
        print(f'O produto: {checagem} aparece {lista_produtos.count(checagem)} vez dentro da lista')
        if lista_produtos.count(checagem) > 0:
            print(f'O produto: {checagem} está na posição {lista_produtos.index(checagem)}')
        break
    lista_produtos.append(produto)