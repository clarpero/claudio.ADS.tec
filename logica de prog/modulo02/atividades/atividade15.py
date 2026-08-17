# Cadastre cinco produtos e suas respectivas quantidades em estoque.
# Ao final, apresente uma mensagem informando quais produtos possuem 
# quantidade igual ou inferior a cinco unidades.

lista = []
estoque = []

for i in range (5):
    produto = input('Informe o nome do produto: ')
    lista.append(produto)
    quantidade = int(input('Informe a quantidade do produto: '))
    estoque.append(quantidade)
    
for num in range(len(estoque)):
    if estoque[num] <= 5:
        print(lista[num], estoque[num])
        