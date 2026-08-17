ANO_ATUAL = 2026
IDADE_MINIMA = 18
nome_usuario = input("Informe seu nome: ")
ano_nascimento = int(input("Informe o seu ano de nascimento: "))
idade = ANO_ATUAL - ano_nascimento

print(f"\nAno atual {ANO_ATUAL}"
      f"Idade minima: {IDADE_MINIMA}"
      f"Nome: {nome_usuario}"
      f"Ano de nascimento: {ano_nascimento}"
      f"Idade: {idade}"
)
