idade = 18
possui_cracha = True
esta_bloqueado = False

print(idade >= 18 and possui_cracha) #True
print(idade < 18 or possui_cracha) #True
print(not esta_bloqueado) #True
print(idade >= 18 and not esta_bloqueado) #True
print(possui_cracha and esta_bloqueado) #False

