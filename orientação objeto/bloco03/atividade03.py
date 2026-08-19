texto = input('Informe uma frase ou uma plavra: ').strip()
texto_limpo = texto.lower().replace(' ', '')
palindromo = texto_limpo[::-1]

print(texto_limpo)
print(palindromo)

if texto_limpo == palindromo:
    print('É um palindromo!')
else:
    print('Não é um palindromo')

