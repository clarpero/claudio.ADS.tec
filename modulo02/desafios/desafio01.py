# Solicite o saldo disponível e o valor desejado para saque. 
# Caso o valor seja menor ou igual ao saldo, informe que a operação foi realizada com sucesso e 
# apresente o novo saldo. Caso contrário, exiba uma mensagem informando saldo insuficiente. 
# Considere também valores inválidos, como saque igual ou menor que zero.
saldo  = 2500
print('Saldo atual: R$ 2,500.00')
saque = float(input('Informe a quantidade para o saque: '))

if saldo >= saque :
    print('Operação foi realizada com sucesso')
    print(f'Novo saldo: R$ {saldo - saque}')
elif saque <= 0:
    print('Valor informado não válido!')
else:
    print('Saldo insuficiente!')
