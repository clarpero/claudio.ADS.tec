# Crie um dicionário contendo informações de um funcionário. 
# Permita ao usuário escolher uma chave para remover. 
# Verifique sua existência antes da operação.

funcionario = {}

funcionario['Nome'] = input('Informe o nome do funcionario: ')
funcionario['Cargo'] = input(f'Informe o cargo do funcionario: {funcionario['Nome']}: ')
funcionario['Setor'] = input(f'Informe o setor do funcionario: {funcionario['Nome']}: ')
funcionario['Salario'] = float(input(f'Informe o salário do funcionario: {funcionario['Nome']}: '))

print('\n::: Chave : Valor :::')
for chave,valor in funcionario.items():
    print([f'{chave} : {valor}'])
    
chave = input('Informe a chave que quer remover: ').upper()

print(f'{funcionario.get(chave, 'Chave não cadastrada.')} : foi removido')

funcionario.pop(chave)

print('\n::: Chave : Valor :::')
for chave,valor in funcionario.items():
    print([f'{chave} : {valor}'])