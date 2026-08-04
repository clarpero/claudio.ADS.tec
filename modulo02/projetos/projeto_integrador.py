dados_do_aluno = []
alunos =[]
turma = []

while True:
    print(
        f'\n1 - Cadastrar aluno'
        f'\n2 - Encerrar')
    opcao = int(input('Informe a opção desejada: '))
    
    match opcao:
        case 1:
            aluno = input('Informe o nome do aluno: ')
            for i in range (3):
                nota = float(input(f'Informe a {i+1}° nota do {nome_do_aluno}'))
                aluno[f'{i+1}° {nota}'] = nota
                print(aluno)
