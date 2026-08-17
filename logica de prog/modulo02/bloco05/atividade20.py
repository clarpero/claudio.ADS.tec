# Solicite ao usuário as notas de um aluno e desenvolva funções separadas para calcular a 
# média, classificar o resultado e apresentar as informações. 
# Organize o programa de forma que cada função possua uma responsabilidade específica.

def media():
    media = 0
    for i in range (3):
        media += int(input(f'Informe a {i+1}º nota do aluno: '))
    media /= 3
    return media 
    

def aprovacao(media):
    if resultado >= 7:
        aprovacao = 'Aprovado'
        
    elif resultado < 5:
        aprovacao = 'Reprovado'
        
    else:
        aprovacao = 'Recuperacao'
    return aprovacao

def resultados(aluno, media, aprovacao):
    print(f'O aluno {aluno}, com a media {media} está {aprovacao}.')

    
aluno = input('Informe o nome do aluno: ')
media = media() #ATRIBUINDO O RESULTADO DA 'DEF MEDIA'
aprovacao = aprovacao(media) #ATRIBUINDO O RESULTADO DA 'DEF APROVACAO(MEDIA)'

resultados(aluno, media, aprovacao) #EXECUTANDO 'DEF RESULTADOS' E SEUS TRES RESPECTIVOS PARAMETROS
