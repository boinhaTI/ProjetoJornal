def cadastrarAdm(usuarios_lista):
    print('CADASTRAMENTO DE LOGIN E SENHA ADM')
    print()
    while True:
        nome = input('Digite seu nome ou digite [0] para cancelar: ')
        if nome == '0':
            print('Cadastro cancelado!')
            break
        loginAdm = input('Cadastre o seu login: ')
        senha = input('Cadastre a sua senha: ')

        # Verifique se o login já existe na lista
        login_existe = False
        for usuario in usuarios_lista:
            if usuario["login"] == loginAdm:
                print('Login já existe.')
                login_existe = True
                break
        if not login_existe:
            DicionarioUsuarioAdm = {"ID": 1, "login": loginAdm, "senha": senha}
            usuarios_lista.append(DicionarioUsuarioAdm)
            print('Usuario cadastrado com sucesso!')
            break
        resp = ' '
        while resp not in 'SsNn':
            resp = input('Deseja continuar cadastrando? Responda [S/N]: ')
        if resp == 'N' or resp == 'n':
             break


def exibirMenuAdm(dicionarioUsuario, dicionarioNoticia):
    while True:
        print('[1] PUBLICAR NOTÍCIAS')
        print('[2] EDITAR NOTÍCIAS')
        print('[3] REMOVER NOTÍCIAS')
        print('[4] SAIR')
        op = int(input('Digite a sua opção: '))

        if op == 1:
            criarNoticia(dicionarioUsuario, dicionarioNoticia)
        elif op == 2:
            editarNoticia(dicionarioUsuario, dicionarioNoticia)
        elif op == 3:
            deletarNoticia(dicionarioUsuario, dicionarioNoticia)
        elif op == 4:
            break

def criarNoticia(dicionarioUsuario, dicionarioNoticia):
    while True:
        titulo = input('Digite o título da notícia: ')
        conteudo = input('Digite o conteúdo da notícia: ')
        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": []}
        dicionarioNoticia["publicacoes"].append(nova_publicacao)
        print('Notícia publicada com sucesso.')

        resp = ' '
        while resp not in 'SsNn':
            resp = input('Deseja adicionar outra publicação? [S/N]:  ')
        if resp == 'N' or resp == 'n':
           break

def editarNoticia(dicionarioUsuario, dicionarioNoticia):
    print('Escolha a publicação que deseja editar:')
    for i, publicacao in enumerate(dicionarioNoticia["publicacoes"]):
        print(f'{i + 1}. {publicacao["titulo"]}')
    escolha = int(input('Escolha um número: '))

    if 1 <= escolha <= len(dicionarioNoticia["publicacoes"]):
        publicacao = dicionarioNoticia["publicacoes"][escolha - 1]
        novo_titulo = input('Digite o novo título (ou pressione Enter para manter o atual): ')
        novo_conteudo = input('Digite o novo conteúdo (ou pressione Enter para manter o atual): ')
        if novo_titulo:
            publicacao["titulo"] = novo_titulo
        if novo_conteudo:
            publicacao["conteudo"] = novo_conteudo
        print('Notícia editada com sucesso.')
        exibirMenuAdm(dicionarioUsuario, dicionarioNoticia)
    else:
        print('Escolha de publicação inválida.')


def deletarNoticia(dicionarioUsuario, dicionarioNoticia):
    while True:
        for i, publicacao in enumerate(dicionarioNoticia["publicacoes"]):
            print(f'{i+1}. {publicacao["titulo"]}')

        escolha = int(input('Digite o número da notícia que deseja deletar (ou 99 para cancelar): '))

        if escolha == 99:
            print('Operação de remoção de notícia cancelada.')
            break

        if 0 <= escolha < len(dicionarioNoticia["publicacoes"]):
            confirmacao = input('Tem certeza de que deseja remover esta notícia? (s/n): ')
            if confirmacao == 's' or confirmacao == 'S':
                publicacao = dicionarioNoticia["publicacoes"].pop(escolha-1)
                print(f'A notícia "{publicacao["titulo"]}" foi removida com sucesso.')

            else:
                print('A remoção da notícia foi cancelada.')
            break
        else:
            print('Número de notícia inválido. Tente novamente.')