# Desenvolva um programa que permita cadastrar dez produtos. 
# Ao final, apresente todos os produtos cadastrados em ordem alfabética.
lista = []

for i in range(10):
    produto = input('Informe o nome o produto: ')
    lista.append(produto)
    
lista.sort()

print(lista)