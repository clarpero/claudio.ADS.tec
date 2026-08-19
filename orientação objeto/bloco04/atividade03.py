import random
pontuacao = 3

while pontuacao < 4 :
    print("### JOKENPÔ ###")
    
    pessoa = input("Escolha: Pedra, Papel ou Tesoura ").upper()
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = random.choice(opcoes)
    
    print(f'Sua escolha: {pessoa}')
    print(f'Escolha do computador: {computador}')
    for pessoa in opcoes():
        if computador == pessoa:
            print('Empate!')
