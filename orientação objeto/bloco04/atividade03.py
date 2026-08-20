import random

pontuacao = 3

while pontuacao < 4:
    print("### JOKENPÔ ###")

    pessoa = input("Escolha: Pedra, Papel ou Tesoura: ").upper()
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = random.choice(opcoes)

    print(f'Sua escolha: {pessoa}')
    print(f'Escolha do computador: {computador}')

    if computador == pessoa:
        print('Empate!')
    elif (
        (pessoa == 'PEDRA' and computador == 'TESOURA') or
        (pessoa == 'PAPEL' and computador == 'PEDRA') or
        (pessoa == 'TESOURA' and computador == 'PAPEL')
    ):
        print('Você venceu!')
        pontuacao += 1
    else:
        print('Você perdeu!')

print("Parabéns! Você atingiu 4 pontos.")