# Solicite ao usuário cinco notas e armazene-as em uma lista. 
# Crie uma função que receba essa lista e retorne a maior nota, a menor nota e a média. 
# Utilize desempacotamento para receber e apresentar os resultados.
def calcular_notas(notas):
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    return maior, menor, media

notas = []

for i in range(5):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

maior, menor, media = calcular_notas(notas)

print(f"\nMaior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
