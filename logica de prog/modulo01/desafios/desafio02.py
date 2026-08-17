distancia = int(input('Informe a distancia percorida em KM (QUILÔMETROS): '))
litros = int(input('Informe a quantidade de gasolina consumida em L (LITROS)'))

media = distancia / litros

print(f'Voce consumiu {litros} L em {distancia} KM'
      f'\nSua media de consumo é {media} L/KM'
      )