# Cadastre as notas de dez estudantes.
# Ao final:
# - apresente todas as notas em ordem crescente;
# - apresente todas as notas em ordem decrescente;
# - informe a maior nota;
# - informe a menor nota;
# - informe a média da turma.
lista_alunos = []
lista_notas = []

for i in range (10):
    aluno = input('Informe o nome do aluno: ')
    lista_alunos.append(aluno)
    nota = int(input('Informe a nota do aluno: '))
    lista_notas.append(nota)
    
lista_notas.sort()
print(f"Ordem crescente: {lista_notas}")

lista_notas.reverse()
print(f"Ordem decrescente: {lista_notas}")

print(f"Maior nota: {max(lista_notas)}")

print(f"Menor nota: {min(lista_notas)}")

print(f"Media da turma: {sum(lista_notas / len(lista_alunos))}")