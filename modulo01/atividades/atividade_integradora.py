produto = input('Informe o produto: ')
preco_unitario = float(input('Informe o preço: '))
quantidade = int(input('Informe a quantidade: '))
percentual_desconto = float(input('Informe o percentual de desconto: '))

subtotal = preco_unitario * quantidade
valor_desconto = subtotal * percentual_desconto/100
total = subtotal - valor_desconto

print(f"\nSubtotal: R$ {subtotal}"
      f"\nValor do desconto: R$ {valor_desconto}"
      f"\nTotal da compra: R$ {total}"
      f"\nQuantidade > 0: {quantidade} {quantidade > 0}"
      f"\nTotal > 100: {total} {total > 100}"
      f"\nProduto tem 'a': {'a' in produto}"    #procuro a letra a dentro da variavel
      f"\nDesconto != None: {valor_desconto is not None}"
      )