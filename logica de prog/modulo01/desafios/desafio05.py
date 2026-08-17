nome = input('Informe o seu nome: ')
salario = float(input('Informe o seu salário atual: '))
percentual = int(input('Informe a porcentagem do reajuste: '))
reajuste = salario * (percentual/100)
novo_salario = salario + reajuste

print(f'Parabens, {nome}! Você recebeu um aumento de {percentual}%!'
      f'\nSeu salário atual de {salario} recebeu um reajuste de {reajuste}.'
      f'\nO seu novo salário é de {novo_salario}'
      )