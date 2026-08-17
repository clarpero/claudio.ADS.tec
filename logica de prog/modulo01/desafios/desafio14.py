nome =  input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))
profissao = input('Informe sua profissão: ')

print(f'\n -----'
      f'\nNome: {nome} | Tipo: {type(nome)} | Nome tem "a": {"a" in nome}'
      f'\nIdade: {idade} | Tipo: {type(idade)} |Idade > 0: {idade > 0}'
      f'\nProfissão: {profissao} | Tipo: {type(profissao)}'
      f'\n -----'
      )