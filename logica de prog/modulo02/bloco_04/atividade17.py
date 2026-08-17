# Cadastre estudantes em uma lista de dicionários, armazenando nome, idade e curso. 
# Em seguida, solicite ao usuário o nome de um estudante, localize seu registro e permita removê-lo após confirmação. 
# Caso o estudante não seja encontrado, informe ao usuário. Ao final, apresente os registros restantes.

alunos = [
            {'NOME' : 'CARLOS',
            'IDADE' : 29,
            'CURSO' : 'MEDICINA'},
            
            {'NOME' : 'ARTHUR',
            'IDADE' : 19,
            'CURSO' : 'MARKETING'},
            
            {'NOME' : 'LIANA',
            'IDADE' : 24,
            'CURSO' : 'FARMACIA'},
            
            {'NOME' : 'JULIA',
            'IDADE' : 27,
            'CURSO' : 'FILOSOFIA'},
]

procura = input('Informe o nome do aluno para procurar: ').upper()


for aluno in alunos:
    if aluno.get('NOME') == procura:
        print('\nAluno encontrado!')
        for chave, valor in aluno.items():
            print(f'{chave} : {valor}')
    else:
        print('Aluno não encontrado!')
        break

for aluno in alunos:
    remover_chave = input('Informe o nome do aluno para remover: ').upper()
    if remover_chave in aluno:
        del aluno[remover_chave]

print(alunos)