#Crie um programa que continue solicitando usuário e senha até que os valores estejam corretos.
# usuario = "admin"
# senha = "python123"
USUARIO = "admin"
SENHA = "python123"

while True :
    usuario = input('Informe o seu usuario: ').lower()
    if usuario != USUARIO:
        print('Usuário invalido, tente novamente!')
        break
    else:
        senha = input('Inform a senha: ').lower()
    if senha != SENHA:
        print('Senha inválida. Tente novamente!')
        break
    else:
        print('Login realizado com sucesso!')