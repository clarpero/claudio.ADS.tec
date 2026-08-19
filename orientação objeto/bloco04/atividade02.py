quantidade = int(input('Informe quantos numeros vai informar: '))
soma =0 

for i in range(quantidade):
    soma+= int(input('Informe o numero para soma: '))
print(f'Total de pontos: {soma}')
print(f'Quantidade de numeros: {quantidade}')
print(f'Media: {soma / quantidade}')