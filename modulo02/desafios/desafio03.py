# Desenvolva um programa que permita cadastrar vários alunos. 
# Para cada estudante, informe seu nome e quatro notas. Ao final do cadastro, apresente um relatório contendo:
# - nome de cada aluno;
# - média final;
# - situação (Aprovado, Recuperação ou Reprovado);
# - maior média da turma;
# - menor média da turma;
# - média geral da turma.
# Utilize listas, estruturas condicionais e laços de repetição para organizar a solução.
lista_alunos =[]
lista_medias = []
lista_situacoes = []

while True:
    print(
        f'\n1 - Cadastrar aluno'
        f'\n2 - Encerrar programa')
    
    opcao = int(input('Informe a operação a ser realizada: '))
    
    match opcao:  
        
        case 1 :
            aluno = input('Informe o nome do aluno: ')
            lista_alunos.append(aluno)
            media = 0
            for i in range(4):
                media += float(input('Informe a media do aluno: '))
            media /= 4
            lista_medias.append(media)
            
            if  media >= 7:                       
                lista_situacoes.append('Aprovado')                       
            elif media >= 5:
                lista_situacoes.append("Recuperação") 
            else:
                lista_situacoes.append("Reprovado") 
            
        case 2:
            print(f'\nPrograma encerrado.\n')
            break
        
        case _ :
            print(f'\nOpção inválida!')
            
print('::::: RELATORIO DE ALUNO :::::')
for aluno, media, situacao in zip(lista_alunos, lista_medias, lista_situacoes):
    print(f'Aluno: {aluno}')
    print(f'Média: {media}')
    print(f'Situação: {situacao}')
    print('\n')

print('\n::::: RELATORIO DA TURMA :::::')
print(f'\nMaior média da turma: {max(lista_medias)}'
      f'\nMenor média da turma: {min(lista_medias)}'
      f'\nMédia geral da turma: {sum(lista_medias) / len(lista_alunos)}')