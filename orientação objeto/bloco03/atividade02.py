frase_completa = input('Informe uma frase: ')
lista = frase_completa.split()

print(f'Quantidade de palavras: {len(lista)}')
print(f'Primeira palavra: {lista[0]}')
print(f'Ultima palavra: {lista[-1]}')