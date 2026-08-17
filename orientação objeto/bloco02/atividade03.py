valor_da_conta = float(input('Informe o valor da conta: '))
quantidade_de_pessoas = int(input('Informe quantas pessoas: '))

valor_unitario = valor_da_conta / quantidade_de_pessoas

print(f'Cada pessoa deve pagar R$ {valor_unitario}')