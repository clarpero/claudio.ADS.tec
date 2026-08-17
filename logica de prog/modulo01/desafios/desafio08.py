altura = int(input('Qual a altura a ser pintada? '))
largura = int(input('Qual a largura a ser pintada? '))
valor = int(input('Qual o valor do seu m²? '))
area = altura * largura
valor_total = valor * area

print(f'Parede: altura de {altura} e uma largura de {largura}'
      f'\nArea a ser pintada: {area}'
      f'\nValor do m²: {valor}'
      f'\nValor toral: {valor_total}'
      )