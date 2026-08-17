# Solicite quatro notas, armazenando-as em uma lista. Ao final, apresente:
# - todas as notas;
# - maior nota;
# - menor nota;
# - média da turma.
# Utilize as funções nativas da linguagem sempre que possível.

lista  =[]
maior_nota = 0
menor_nota = 100
media = 0


for i in range (4):
    nota_aluno = int(input("informe a nota do aluno: "))
    lista.append(nota_aluno)
    if nota_aluno > maior_nota:
        maior_nota = nota_aluno
    if nota_aluno < menor_nota:
        menor_nota = nota_aluno
    media += nota_aluno / (len(lista))

print(f'\nTodas as notas: {lista}'
      f'\nMaior nota: {maior_nota}'
      f'\nMenor nota: {menor_nota}'
      f'\nMedia: {media:.1f}')