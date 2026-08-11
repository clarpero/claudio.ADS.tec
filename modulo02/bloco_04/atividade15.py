# Cadastre contatos em uma lista de dicionários, armazenando nome, telefone e e-mail. 
# Em seguida, solicite ao usuário o nome de um contato, pesquise-o na lista e apresente seus dados. 
# Caso o contato não seja encontrado, informe ao usuário.

contatos =[
        {'NOME' : 'LUCIANO',
        'TELEFONE' : '86 9999-2020',
        'EMAIL' : 'luciano@gmail.com'},
        
        {'NOME' : 'LUIZ',
        'TELEFONE' : '85 9898-6363',
        'EMAIL' : 'luiz@gmail.com'},
        
        {'NOME' : 'ANA',
        'TELEFONE' : '81 9977-6633',
        'EMAIL' : 'ana@gmail.com'}
]

procura = input('Informe o nome do contato para procurar: ').upper()

while True:
    for contato in contatos:
        if contato.get('NOME') == procura:
            print('\nContato encontrado!\n')
            for chave, valor in contato.items():
                print(f'{chave} : {valor}')
            print(end='\n')
    else:
        print('Contato não encontrado!')
    break

