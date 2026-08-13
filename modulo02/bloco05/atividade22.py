# Cadastre produtos utilizando uma lista de dicionários. Crie uma função que receba a lista de produtos e o nome que será pesquisado. 
# A função deverá retornar o dicionário correspondente quando o produto for encontrado ou None quando não existir.

def lista_de_produtos ():
    return [{'NOME' : 'ARROZ', 'PRECO' : 12.99, 'CATEGORIA' : 'ALIMENTO'},
            {'NOME' : 'FEIJAO', 'PRECO' : 9.49, 'CATEGORIA' : 'ALIMENTO'},
            {'NOME' : 'TOMATE', 'PRECO' : 3.99, 'CATEGORIA' : 'ALIMENTO'},
            {'NOME' : 'ALFACE', 'PRECO' : 7.99, 'CATEGORIA' : 'ALIMENTO'},
            {'NOME' : 'OVO', 'PRECO' : 15.99, 'CATEGORIA' : 'ALIMENTO'}]
    
def procurando_produtos(lista, procurando):
    for indice, produto in enumerate(lista):    #INDICE(indicando a posição do dicionario) PRODUTO(selecionando o dicionario)
        if produto.get('NOME') == procurando:
            print(f'\nProduto encontrado no índice nº {indice}')
    if produto.get('NOME') != procurando:
        print(f'\nProduto não encontrado')
        
lista = lista_de_produtos()

procurando = input('Informe o produto para procurar: ').upper()

indice = procurando_produtos(lista, procurando)

