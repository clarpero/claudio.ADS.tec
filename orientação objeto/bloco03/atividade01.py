nome_completo = input('Informe o nome completo: ')
nomes = nome_completo.split()

excecoes = ['de', 'do', 'da', 'dos', 'das', 'e']
nome_formatado = []

for nome in nomes:
    if nome in excecoes: 
        nome_formatado.append(nome)
    else:
        nome_formatado.append(nome.capitalize())

for nome in nome_formatado:
    print(nome, end=' ')

for i in nomes:
    if len(i) > 2:
        print({i[0].upper()}, end='. ')