lista = []
lista_par = []
lista_impar = []
for i in range(10):
    numero = int(input(f'Informe o {i+1}º numero: '))
    lista.append(numero)

print(f'Lista completa: {lista}')

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f'Numeros pares: {lista_par}')
print(f'Numeros impares: {lista_impar}')