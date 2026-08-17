# Solicite um número inteiro e apresente sua tabuada 
# de 1 até 10 utilizando um laço de repetição.
num = int(input('Informe um numero inteiro: '))

for i in range (0 , 9):
    print(f'{num} x {i+1} = {num * (i+1)}')