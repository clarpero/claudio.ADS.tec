nome_vendedor = input('Informe o nome do vendedor: ')
nome_cliente = input('Informe o nome do cliente: ')
produto_vendido = input('Informe o produto vendido: ')
quantidade = int(input('Informe a quantidade vendida: '))
valor_unit = float(input('Informe o valor do produto: '))
desconto = int(input('Informe o percentual do desconto: '))

subtotal = quantidade * valor_unit
desconto_real = subtotal * (desconto/100)
valor_total = subtotal - desconto_real

print(f'\nDados da operação: '
      f'\nNome do vendedor: {nome_vendedor}'
      f'\nNome do cliente: {nome_cliente} | Cliente tem "a": {"a" in nome_cliente}'
      f'\nProduto: {produto_vendido}'
      f'\nQuantidade: {quantidade}'
      f'\nValor unitário: {valor_unit}'
      f'\nSubtotal: {subtotal:.2f} | Subtotal > 500 {subtotal > 500}'
      f'\nDesconto: {desconto} = {desconto_real} | Desconto == None: {desconto is None}'
      f'\nValor final: {valor_total} | Valor > 500 {valor_total > 500}'
      )