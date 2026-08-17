estudante = input('Informe o nome do aluno: ')
idade = int(input('Informe a idade do aluno: '))
cidade = input('Informe a cidade do aluno: ')
altura = float(input('Informe a altura do aluno: '))

print(f'\n ----- \n Dados do aluno \n ----- \n'
      f'Nome: {estudante} | {type(estudante)}'
      f'\nIdade: {idade} | {type(idade)}'
      f'\nCidade: {cidade} | {type(cidade)}'
      f'\nAltura: {altura} | {type(altura)}'
      )