# # Cadastre o nome de cinco alunos e a média final de cada um.
# # Após o cadastro, apresente um relatório contendo:
# # - nome;
# # - média;
# # - situação (Aprovado, Recuperação ou Reprovado).
# # Ao final, informe:
# - quantidade de aprovados;
# - quantidade de alunos em recuperação;
# - quantidade de reprovados.
alunos = []
medias = []
situacao_geral = []

for i in range (5):
    aluno = input('Informe o nome do aluno: ')
    alunos.append(aluno)
    media = float(input('Informe a média do aluno: '))
    medias.append(media)
    if media < 5:
        situacao_geral.append('Reprovado'.lower())
    elif media >= 7:
        situacao_geral.append('Aprovado'.lower())
    else:
        situacao_geral.append('Recuperaçao'.lower())

print(f'Aprovados: {situacao_geral.count('aprovado')}')
print(f'Recuperação: {situacao_geral.count('recuperaçao')}')
print(f'Reprovados: {situacao_geral.count('reprovado')}')