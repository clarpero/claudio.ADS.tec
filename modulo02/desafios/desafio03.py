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
while True:
    print(
        f'\n1 - Cadastrar aluno'
        f'\n2 - Ver maior média'
        f'\n3 - Ver menor média'
        f'\n4 - Ver média geral da turma')
    
    opcao = int(input('Informe a operação a ser realizada: '))
    
    match opcao:  
        
        case 1 :
            aluno = input('Informe o nome do aluno: ')
            lista_alunos.append(aluno)
            media = float(input('Informe a media do aluno: '))
            lista_medias.append(media)
            
        case 2:
            print(f'\nA maior média da turma é: {max(lista_medias)}')
            
        case 3 :
            print(f'\nA menor média da turma é: {min(lista_medias)}')
            
        case 4:
            print(f'\nA média geral da turma é: {sum(lista_medias) / len(lista_medias)}')
        
        case _ :
            print('\nOpção inválida!')