# Crie uma função que receba o nome de uma pessoa como parâmetro e apresente uma saudação personalizada. 
# Solicite o nome ao usuário e utilize-o na chamada da função.
def greetings(name):
    print(f'Saudações {name}')
    
name = input('Informe o seu nome: ')
print(greetings())