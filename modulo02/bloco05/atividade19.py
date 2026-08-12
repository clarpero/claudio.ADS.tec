# Crie funções separadas para somar, subtrair, multiplicar e dividir dois números. 
# Cada função deverá receber os números como parâmetros e retornar o resultado da operação. 
# Solicite os valores ao usuário e utilize as funções para realizar os cálculos.
def somando(x, y):
    print(f'{x} + {y} = {x + y}')
    
def subtraindo(x, y):
    print(f'{x} - {y} = {x - y}')
    
def multipicando(x, y):
    print(f'{x} x {y} = {x * y}')

def dividindo(x, y):
    print(f'{x} / {y} = {x / y}')
    
x = int(input('Informe um numero para calcular: '))
y = int(input('Informe outro numero para calcular: '))

print(somando(x,y))
print(subtraindo(x,y))
print(multipicando(x,y))
print(dividindo(x,y))
    
