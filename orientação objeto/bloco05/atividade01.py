meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

while True:
    
    try :
        escolha = int(input('Digite um número de 1 a 12: '))
        if 1 <= escolha <=12:
            break
        print('Valor inválido. Digite apenas numeros inteiros de 1 a 12.')
    except ValueError:
        print('Entrada inválida. Digite um numero inteiro.')


for c in range(len(meses)):
    if escolha == c + 1:
        print(f'O mês correspondente ao número {escolha} é {meses[c]}')