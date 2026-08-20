lista_cadastros = []
media_idade = 0
cadastros = int(input("Digite o número de cadastros a serem inseridos: "))

for i in range(cadastros):
    nome = input(f"Digite o nome do {i + 1}º cadastro: ").lower()
    idade = int(input(f"Digite a idade do {i + 1}º cadastro: "))

    cadastro = []
    cadastro.append(nome)
    cadastro.append(idade)
    lista_cadastros.append(cadastro)
    media_idade += idade
    
print(f"Cadastros inseridos: {cadastros}")
print(f'A média de idade dos cadastros é: {media_idade / cadastros:.2f} anos')

for nome, idade in lista_cadastros:
    if idade > media_idade / cadastros:
        print(f"{nome.capitalize()} tem idade acima da média.")