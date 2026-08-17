nome = input('Informe o seu nome: ')
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))
imc = peso / (altura*altura)

print(f'Olá, {nome}!'
      f'\n Sua altura é {altura}'
      f'\n Seu peso é {peso}'
      f'\n Seu imc é {imc:.2f}'
      )