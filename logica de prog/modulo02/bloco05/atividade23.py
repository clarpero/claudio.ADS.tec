# Cadastre produtos em uma lista de dicionários. Crie uma função que receba a lista, o nome do produto e a nova quantidade em estoque. 
# Caso o produto seja encontrado, atualize sua quantidade e retorne True. Caso contrário, retorne False.

lista_de_produtos = [
    {'NOME' : 'ARROZ', 'PRECO' : 12.99, 'ESTOQUE' : 'ALIMENTO'},
    {'NOME' : 'FEIJAO', 'PRECO' : 9.49, 'ESTOQUE' : 'ALIMENTO'},
    {'NOME' : 'TOMATE', 'PRECO' : 3.99, 'ESTOQUE' : 'ALIMENTO'},
    {'NOME' : 'ALFACE', 'PRECO' : 7.99, 'ESTOQUE' : 'ALIMENTO'},
    {'NOME' : 'OVO', 'PRECO' : 15.99, 'ESTOQUE' : 'ALIMENTO'}]

def adicionando_produtos(lista, nome, quantidade):
    procurando = input('Informe o produto para procura: ').upper()
    for indice, produto in enumerate(lista_de_produtos):    #INDICE(indicando a posição do dicionario) PRODUTO(selecionando o dicionario)
        if produto.get('NOME') == procurando:
            produto['ESTOQUE'] = int(input('Informe o estoque do produto: '))
            return True
    if produto.get('NOME') != procurando:
        print(f'\nProduto não encontrado')
   


adicionando_produtos(lista_de_produtos,"FEIJÃO", 80)
print(lista_de_produtos)

