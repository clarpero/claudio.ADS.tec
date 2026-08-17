# primeira_compra = float(input('Informe o valor da compra: '))
# segunda_compra = float(input('Informe o valor da segunda compra: '))
# soma = primeira_compra + segunda_compra

# print(f'O valor total da compra {soma}')

soma = 0
for i in range (2):
    soma += float(input(f'Informe o valor da {i+1}º compra: '))
print(soma)