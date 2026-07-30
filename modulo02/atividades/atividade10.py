# Desenvolva um programa que solicite o nome de cinco alunos, armazenando-os em uma lista. 
# Ao final, apresente todos os nomes cadastrados.

lista = []

for i in range (5):
    nome_aluno = input('Informe o nome do aluno: ')
    lista.append(nome_aluno)
print(lista)