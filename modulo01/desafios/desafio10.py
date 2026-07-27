distancia_total = int(input('Informe a distancia da viagem em KM: '))
consumo_medio = int(input('Informe o consumo médio do veículo: '))
preco = float(input('Informe o preço do combustível: '))

litros = distancia_total / consumo_medio
valor_final = litros * preco

print(f'Distancia a percorrer: {distancia_total}'
      f'\nQuantidade de combustivél: {litros}'
      f'\nValor total: {valor_final}'
      )