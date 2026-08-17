nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')
curso = input('Digite seu curso: ')

print("Bem-vindo", end=" ") #end = "" > encerro a linha sem a necessidade de um \n no inicio da proxima
print("ao Python!")         # sep = " " > incluo separação automatica entre as exibições
print(nome, idade, cidade, curso, sep=" | ")    