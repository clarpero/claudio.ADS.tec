#Atividade 06 — Investigação de tipos
valor1 = 25
valor2 = "25"
valor3 = 25.0
valor4 = True
valor5 = None

print("V1", valor1)
print(type(valor1))
print(isinstance(valor1, int))

print("\nV2", valor2)
print(type(valor2))
print(isinstance(valor2, str))

print("\nV3", valor3)
print(type(valor3))
print(isinstance(valor3, float))

print("\nV4", valor4)
print(type(valor4))
print(isinstance(valor4, bool))

print("\nV5", valor5)
print(type(valor5))
print(isinstance(valor5, type(None)))