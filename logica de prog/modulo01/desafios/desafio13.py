cliente = input('Informe o nome: ')
quantidade = int(input('Informe a quantidade de ingressos: '))
preco_unt = float(input('Informe o valor do ingresso: '))
valor_total = quantidade * preco_unt

print(f'\n ----- \n Dados da compra \n ----- \n'
      f'Nome: {cliente} | {type(cliente)}'
      f'\nQuantidade: {quantidade} | {type(quantidade)}'
      f'\nPreço unitário: {preco_unt} | {type(preco_unt)}'
      f'\nValor total: {valor_total} | {type(valor_total)}'
      )