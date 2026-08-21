jogador ={}


jogador['nome'] = input('Informe o nome do jogador: ')
jogador['partidas'] = int(input('Informe o número de partidas: '))
jogador['total_de_gols'] = []

for i in range (jogador['partidas']):
    gol = int(input(f'Quantidade de gols feito na {i+1}º partida: '))
    jogador['total_de_gols'].append(gol)
    
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
print(f'Total de gols: {sum(jogador["total_de_gols"])}')
for chave, valor in enumerate(jogador['total_de_gols']):
    print(f'Na partida {chave+1} fez {valor} gols.')