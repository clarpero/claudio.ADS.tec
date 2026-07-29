# Solicite um número inteiro ao usuário e apresente a contagem regressiva até zero

num = int(input('Informe um numero para contagem regressiva: '))

while num >= 0: #enquanto for maior que 0, continua a contagem 
    print(num)  #print a variavel de entrada
    num -= 1    #atualiza a variavel com -1