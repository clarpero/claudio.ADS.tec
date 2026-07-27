produto = input('Informe o item de compra: ')
preco_und = int(input('Informe o preço: '))
quantidade = int(input('Informe a quantidade: '))
desconto = int(input('Informe a porcentagem de desconto: '))
subtotal = preco_und * quantidade
desconto_total = (desconto/100) * subtotal
valor_final = subtotal - desconto_total

print(f'\n = = = = = = = = = = = = = =\nResumo da compra:\n = = = = = = = = = = = = = =\n'
      f'Produto: {produto}'
      f'\nQuantidade: {quantidade}'
      f'\nSubtotal: {subtotal}'
      f'\nDesconto: {desconto}% = {desconto_total}'
      f'\nValor final da compra: {valor_final}' 
      f'\n = = = = = = = = = = = = = =\n'    
      )


