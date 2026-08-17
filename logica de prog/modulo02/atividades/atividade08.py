# Solicite ao usuário um número inteiro positivo.
# Calcule a soma de todos os números entre **1** e o valor informado.

num = int(input('Informe um numero inteiro positivo: '))
soma = 0
contador  = 1

while contador <= num:
    soma += contador
    contador +=1
print(soma)