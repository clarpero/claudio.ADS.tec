# Desenvolva um programa que solicite o valor de cada venda e continue 
# recebendo novos valores até que o usuário informe 0. Ao finalizar, apresente:
# - quantidade de vendas realizadas;
# - valor total vendido;
# - valor médio das vendas;
# - maior venda registrada;
# - menor venda registrada.
valor_da_venda = float
total_de_vendas = 0
media_vendida = 0
valor_total = 0
maior_valor = 0
menor_valor = 99999

while (valor_da_venda != 0) :    
    
    valor_da_venda = float(input('Informe o valor da venda ou digite 0 para parar: '))
    
    if valor_da_venda == 0 : 
            
        print(f'\nNumero de vendas: {total_de_vendas:.2f}'
              f'\nValor total das vendas: {valor_total:.2f}'
              f'\nMedia das vendas: {media_vendida:.2f}'
              f'\nMaior valor vendido: {maior_valor:.2f}'
              f'\nMenor valor vendido: {menor_valor:.2f}')
        break
    
    if valor_da_venda > maior_valor :
        maior_valor = valor_da_venda
        
    if valor_da_venda < menor_valor :
        menor_valor = valor_da_venda
    
    total_de_vendas += 1
    valor_total += valor_da_venda
    media_vendida = valor_total / total_de_vendas