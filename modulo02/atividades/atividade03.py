# Solicite o nome, peso e altura do usuário.
# Calcule o IMC e informe a classificação utilizando estruturas condicionais.
# Utilize a tabela oficial da OMS para definir as faixas.

nome = input("Qual seu nome? ")
altura = float(input("Qual sua altura em metros (Ex.: 1.75)? "))
peso = floar(input("Qual seu peso? "))

imc = peso / (altura * altura)

if imc >= 40 :
    print(f'Nome: {nome}: Obesidade de Classe 3 (mórbida/grave)')
elif imc >= 35 :
    print(f'Nome: {nome}: Obesidade de Classe 2 (severa)')
elif imc >= 30 :
    print(f'Nome: {nome}: Obesidade de Classe 1 (leve)')
elif imc >= 25 :
    print(f'Nome: {nome}: Excesso de peso (sobrepeso)')
elif imc >= 18.5 :
    print(f'Nome: {nome}: Peso normal (saudável)')
else :
    print(f'Nome: {nome}: Baixo peso')
    
    