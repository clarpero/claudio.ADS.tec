# Cadastre inicialmente os seguintes alunos:
# "Ana","Carlos","Maria","Pedro","Lucas"
# Solicite um nome ao usuário e informe se ele está presente na lista. Caso esteja, apresente também sua posição.

lista = [
    "Ana",
    "Carlos",
    "Maria",
    "Pedro",
    "Lucas"
]

for nome in lista:
    nome_digitado = input('Informe o nome para procura: ').lower()
    if nome.lower() == nome_digitado:
        print(f'{nome} está presente na posição {lista.index(nome)}')
    else:
        print('O nome não está presente!')
