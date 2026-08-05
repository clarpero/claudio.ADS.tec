alunos =[]

while True:                                         #iniciando o laço de repetição
    print(                                          #iniciando o menu cadastro
        f'\n1 - Cadastrar aluno'
        f'\n2 - Encerrar')
    opcao = int(input('Informe a opção desejada: '))    #interagindo com o usuário
    
    match opcao:                                        #iniciando laço de repetição (procura)
        case 1:     #O laço abaixo acontece APENAS SE o usúario interagir digitando 1
            
            nome = input('Informe o nome do aluno: ')   #interagindo com o usuário
            dados_do_aluno =[nome]                      #inserindo dados em uma lista
            
            for i in range (3):                                             #iniciando laço de interação com usuário
                nota = float(input(f'Informe a {i+1}° nota do {nome}: '))   #interagindo com o usuário
                dados_do_aluno.append(nota)                                 #inserindo dados em uma lista
                
            alunos.append(dados_do_aluno)                 #inserindo todos os dados coletados no "CASE 1" dentro de uma lista
              
        case 2:     #O laço abaixo acontece APENAS SE o usúario interagir digitando 2
            if not alunos:                          #iniciando uma condicional se não houver dados na lista
                print('Nenhum aluno cadastrado.')
                break                               #encerrando o laço caso a condicional acima seja atendida
            
            print('\n :::::: Relatório de Alunos ::::::')   #iniciando o print(saída de dados) para relatório
            
            medias = []                                     #criando uma nova lista para armazenamento de dados
            aprovados = 0                                   #criando variavél para contagem
            
            for aluno in alunos:                           #iniciando laço para contagem e atribuição
                nome = aluno[0]                            #nome do aluno vai ser = ao primeiro dado encontrado dentro de alunos[0]
                nota1 = aluno[1]                           #nome do aluno vai ser = ao segundo dado encontrado dentro de alunos[1]
                nota2 = aluno[2]                           #nome do aluno vai ser = ao terceiro dado encontrado dentro de alunos[2]
                nota3 = aluno[3]                           #nome do aluno vai ser = ao quarto dado encontrado dentro de alunos[3]
                media = (nota1 + nota2 + nota3) / 3        #definindo media do aluno
                medias.append(media)                       #inserindo a media dentro de uma lista
                
                
            if  media >= 7:                         #iniciando condicional para aprovados
                situacao = "Aprovado"
                aprovados += 1                      #contando o numero de aprovados caso a condicional acima seja atendida (+=1)
            elif media >= 5:
                situacao = "Recuperacao"
            else:
                situacao = "Reprovado"
                
            print(f'Aluno: {nome}')
            print(f'Notas: {nota1:.1f} | {nota2:.1f} | {nota3:.1f}')
            print(f'Média: {media:.1f}')
            print(f'Situação: {situacao}')
            
            print('\n :::::: Relatório da Turma ::::::')
            total_de_alunos = len(alunos)                               #definindo total de aluno = comprimento da lista alunos
            media_geral = sum(medias) / total_de_alunos                 #somando todas as medias da lista e dividindo pelo total de alunos
            maior_media = max(medias)                                   #usando função MAX para definir a maior media
            menor_media = min(medias)                                   #usando função MIN pra definir a menor media
            percentual_aprovados = (aprovados / total_de_alunos) * 100  #definindo percentual de aprovação dividindo o contados APROVADOS pelo total de alunos e * 100
            
            print(f'Quantidade total de alunos: {total_de_alunos}')
            print(f'Media geral da turma: {media_geral:.1f}')
            print(f'Maior média: {maior_media:.1f}')
            print(f'Menor média: {menor_media:.1f}')
            print(f'Percentual de aprovados: {percentual_aprovados}% de aproveitamento')
            break
        case _ :
            print('Opção inválida!')
            
            
            
            
