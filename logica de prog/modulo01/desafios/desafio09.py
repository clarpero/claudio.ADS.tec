valor_total = float(input('Informe o valor da compra: '))
valor_entregue = float(input('Informe o valor dado: '))
valor_troco = valor_total - valor_entregue

print(f'Valor da compra: {valor_total} reais'
      f'\n- Valor pago: {valor_entregue} reais')

if valor_troco > 0: 
    print(f'Faltam: {valor_troco} reais')
else: 
    print(f'Valor do troco: {valor_troco} reais')