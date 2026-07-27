produto = "Caneca de Café"
quantidade = 50
preco = 12.9
categoria = "Utensílios Domésticos"
desconto = None
if quantidade > 0 :
    disponibilidade = True
else:
    disponibilidade = False

print(f'\nProduto: ', type(produto))
print(f'Quantidade: ', type(quantidade))
print(f'Preco: ', type(preco))
print(f'Categoria: ', type(categoria))
print(f'Disponibilidade: ', type(disponibilidade))
print(f'Desconto: ', type(desconto))

desconto = 10
print(type(desconto))

#O tipo de variável mudou porque o Python é uma linguagem verátil
#com uma tipagem dinâmica que 