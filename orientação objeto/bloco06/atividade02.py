heroi = {}
lista_de_herois = []
quantidade_de_herois = int(input('Informe a quantidade de herois para cadastrar: '))

for i in range (quantidade_de_herois):
    print(f'Informações sobre o {i+1}º Heroi:')
    heroi['Nome'] = input('Infome o nome do heroi: ')
    heroi['Poder'] = input('Informe o poder do heroi: ')
    heroi['Forca'] = int(input('Informe o nivel de força do heroi: '))
    heroi['Cidade'] = input('Informe a cidade que o heroi protege: ')
    lista_de_herois.append(heroi)

for heroi in lista_de_herois:
    if heroi['Forca'] <= 40:
        heroi['Categoria'] = 'Iniciante'
    elif heroi['Forca'] > 7 :
        heroi['Categoria'] = 'Lendário'
    else:
        heroi['Categoria'] = 'Experiente'

for heroi in lista_de_herois:
    for chave, valor in lista_de_herois.items():
        print('## ## Dados do Héroi ## ##')
        print(f'{chave}: {valor}')


