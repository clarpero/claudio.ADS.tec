nome = input('Informe o nome do aluno(a): ')
primeira_nota = int(input('Informe a primeira nota: '))
segunda_nota = int(input('Informe a segunda nota: '))
terceira_nota = int(input('Informe a terceira nota: '))
quarta_nota = int(input('Informe a quarta nota: '))
media_aluno = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f'Aluno(a): {nome}'
      f'\nNota 1: {primeira_nota}'
      f'\nNota 2: {segunda_nota}'
      f'\nNota 3: {terceira_nota}'
      f'\nNota 4: {quarta_nota}'
      f'\nMedia: {media_aluno}'
      )