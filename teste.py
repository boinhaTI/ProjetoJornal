adms_cadastrados = {}
usuarios_cadastrados = {}
op = 0

while True:
    print('''[1] CADASTRO ADM
[2] CADASTRO USUÁRIO
[3] EFETUAR LOGIN
[4] SAIR''')
    op = int(input('Digite a sua opção: '))

    if op == 1:
        print()
        print('PREENCHA O CADASTRO ADM')
        print()
        while True:
            login = input('Cadastre o seu login: ')
            senha = input('Cadastre a sua senha: ')
            adms_cadastrados[login] = senha

            resp = input('Deseja continuar cadastrando? Responda [S/N]: ')
            if resp.lower() != 's':
                break

    elif op == 2:
        print()
        print('PREENCHA O CADASTRO USUÁRIO')
        print()
        loginCadaUsuario = input('Digite o seu login: ')
        senhaCadaUsuario = input('Digite a sua senha: ')
        usuarios_cadastrados[loginCadaUsuario] = senhaCadaUsuario

    elif op == 3:
        nome_login = input('Digite o seu login: ')
        senha_login = input('Digite a sua senha: ')
        if nome_login in adms_cadastrados and adms_cadastrados[nome_login] == senha_login:
            longado = True
            print('Parabéns, você está logado como ADM!!')
            break
        else:
            print('Usuário e/ou senha incorretos.')
            if longado == True:
                while True:
                    print('''[1] INSERIR NOTÍCIA
                    [2] LISTAR NOTÍCIAS
                    [3] SAIR''')
                    op = int(input('Digite a sua opção: '))


    elif op == 4:
        break

    else:
        print('Opção inválida. Tente novamente.')

print('Adms cadastrados:', adms_cadastrados)
print('Usuários cadastrados:', usuarios_cadastrados)
