alunos =[]
medias = []
aprovados = []

while True:                                         
    print(                                          
        f'\n1 - Cadastrar aluno'
        f'\n2 - Encerrar')
    opcao = int(input('Informe a opção desejada: '))    
    
    match opcao:                                        
        case 1:     
            
            nome = input('Informe o nome do aluno: ')   
            dados_do_aluno =[nome]                      
            
            for i in range (3):                                             
                nota = float(input(f'Informe a {i+1}° nota do {nome}: '))   
                dados_do_aluno.append(nota)                                 
            
            media = sum(dados_do_aluno[1:4]) / 3 
            dados_do_aluno.append(media)
            medias.append(media)
            
            #print(dados_do_aluno)
            if  media >= 7:                       
                dados_do_aluno.append("Aprovado")
                aprovados.append('Aprovado')                       
            elif media >= 5:
                dados_do_aluno.append("Recuperação") 
            else:
                dados_do_aluno.append("Reprovado") 
                                          
            alunos.append(dados_do_aluno)                 
              
        case 2:     
            if not alunos:                          
                print('Nenhum aluno cadastrado.')
            break
        
        case _ :
            print('Opção inválida!')           
            
            
for i in range(len(alunos)):
    print('\n :::::: Relatório do Aluno ::::::')       
    print(f'Aluno: {alunos[i][0]}')
    print(f'Notas: {alunos[i][1]:.1f} | {alunos[i][2]:.1f} | {alunos[i][3]:.1f}')
    print(f'Média: {alunos[i][4]:.1f}')
    print(f'Situação: {alunos[i][5]}')
            
print('\n :::::: Relatório da Turma ::::::')
print(f'Quantidade total de alunos: {len(alunos)}')
print(f'Media geral da turma: {(sum(medias) / len(alunos)):.1f}')
print(f'Maior média: {max(medias):.1f}')
print(f'Menor média: {min(medias):.1f}')
print(f'Percentual de aprovados: {(len(aprovados) / len(alunos)) * 100 }% de aproveitamento.')
