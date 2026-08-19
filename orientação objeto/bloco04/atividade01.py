a = int(input('Informe o valor do lado do triangulo: '))
b = int(input('Informe o valor do lado do triangulo: '))
c = int(input('Informe o valor do lado do triangulo: '))

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    print('O triangulo é possivel!')
    if (a == b) and (a == c) and (b == c):
        print('É um triangukllo equilátero!')
    elif (a == b) and (a == c) or (b == c):
        print('É um triangulo isósceles!')
    else:
        print('É um triangulo escaleno')
else:
    print('Não é possivel formar triangulo!')
