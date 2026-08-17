# Solicite a nota final de um estudante e informe sua situação conforme os critérios abaixo:
# nota maior ou igual a 7: aprovado;
# nota maior ou igual a 5 e menor que 7: recuperação;
# nota menor que 5: reprovado.

nota = float(input('Informe a sua nota: '))

if nota >= 7:
    print('Parabens, aprovado!')
elif (nota >= 5) and (idade < 7):
    print('Voce está de recuperção!')
else :
    print('Voce está reprovado!')