import geral
def cadastrarAdm(usuarios_lista):
    print('CADASTRAMENTO DE LOGIN E SENHA ADM')
    print()
    while True:
        nome = input('Digite seu nome ou digite [0] para cancelar: ')
        if nome == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif nome == '':
            continue
        loginAdm = input('Cadastre o seu login (ou digite [0] para cancelar:')
        if loginAdm == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif loginAdm == '':
            print('Login não pode estar em branco. Tente novamente.')
            continue
        senha = input('Cadastre o seu senha (ou digite [0] para cancelar: ')
        if senha == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif senha == '':
            print('Senha não pode estar em branco. Tente novamente.')

        else:
            login_existe = False              # Verificar se o login já existe na lista
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



                # resp = ' '
                # while resp not in 'SsNn':
                #     resp = input('Deseja continuar cadastrando? Responda [S/N]: ')
                # if resp == 'N' or resp == 'n':
                #      break



def exibirMenuAdm(usuariolista, dicionarioUsuario, dicionarioNoticia):
    while True:
        print('BEM VINDO AO MENÚ ADMINISTRDOR')
        print()
        print('[1] PUBLICAR NOTÍCIAS')
        print('[2] EDITAR NOTÍCIAS')
        print('[3] REMOVER NOTÍCIAS')
        print('[4] SAIR')
        op = input('Digite a sua opção: ')
        if op.isdigit():
            op = int(op)
            if op == 1:
                criarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 2:
                editarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 3:
                deletarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 4:
                break
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 4.')

        else:
            print('Opção Inválida! Não aceitamos campo em branco e nem letras alfabeticas.\n'
                  '    ---> Por favor digite os valores conforme o "MENU". <---')



def criarNoticia(dicionarioUsuario, dicionarioNoticia):
    while True:
        titulo = input('Digite o título da notícia ou [0] para cancelar: ')
        if titulo == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        if titulo == '':
            print('Opção Inválida! Não aceitamos campo em branco')
            continue
        else:
            conteudo = input('Digite o conteúdo da notícia ou [0] para cancelar: ')
            if conteudo == '0':
                print('Cadastro cancelado pelo usuário!')
                break
            if conteudo == '':
                print('Opção Inválida! Não aceitamos campo em branco.Tente novamente!')
                continue
        # Assumindo que dicionarioUsuario é o nome de usuário
        nome_usuario = dicionarioUsuario

        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": [], "usuario": nome_usuario}
        dicionarioNoticia["publicacoes"].append(nova_publicacao)

        print('Notícia publicada com sucesso.')
        print(dicionarioNoticia)


        # resp = ' '
        # while resp not in 'SsNn':
        #     resp = input('Deseja adicionar outra publicação? [S/N]:  ')
        # if resp == 'N' or resp == 'n':
        #    break




def editarNoticia(dicionarioUsuario, dicionarioNoticia):

    # Codigo para verificar se o usuário não está presente em nenhuma notícia
    if dicionarioUsuario not in [noticia.get("usuario") for noticia in dicionarioNoticia["publicacoes"]]:
        print('Você não possui nenhuma notícia publicada. Vamos publicar a primeira notícia para você.')
        criarNoticia(dicionarioUsuario, dicionarioNoticia)
        return

    listnews = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]



    for i in range(len(listnews)):
        print(f'{i} - {listnews[i]["titulo"]}')
        print(f'{listnews[i]["conteudo"]}\n')
    else:
        print('Você possui notícia publicada.')

    while True:
        print('Escolha a publicação que deseja editar:')
        for i, publicacao in enumerate(dicionarioNoticia["publicacoes"]):
            print(f'{i + 1}. {publicacao["titulo"]}')

        escolha = int(input('Escolha um número para editar ou 0 para sair '))

        if 1 <= escolha <= len(dicionarioNoticia["publicacoes"]):
            publicacao = dicionarioNoticia["publicacoes"][escolha - 1]
            novo_titulo = input('Digite o novo título (ou pressione Enter para manter o atual): ')
            novo_conteudo = input('Digite o novo conteúdo (ou pressione Enter para manter o atual): ')
            if novo_titulo:
                publicacao["titulo"] = novo_titulo
            if novo_conteudo:
                publicacao["conteudo"] = novo_conteudo
            print('Notícia editada com sucesso.')
            break
        else:
            print('Escolha de publicação inválida.')
            break
def deletarNoticia(dicionarioUsuario, dicionarioNoticia):

    while True:
        numeroPublicacao = len(dicionarioNoticia["publicacoes"])
        if numeroPublicacao == 0:
            print('Não há notícias para deletar.')
            break

        for i, publicacao in enumerate(dicionarioNoticia["publicacoes"], start=1):
            print(f'{i}. {publicacao["titulo"]}')

        escolha = int(input('Digite o número da notícia que deseja deletar (ou 0 para cancelar): '))

        if escolha == 0:
            print('Operação de remoção de notícia cancelada.')
            break

        if 1 <= escolha <= numeroPublicacao:
            confirmacao = input('Tem certeza de que deseja remover esta notícia? (S/N): ')
            if confirmacao == 's' or confirmacao == 'S':
                publicacao = dicionarioNoticia["publicacoes"].pop(escolha-1)
                print(f'A notícia "{publicacao["titulo"]}" foi removida com sucesso.')

            else:
                print('A remoção da notícia foi cancelada pelo usuário.')
            break
        else:
            print('Número de notícia inválido. Tente novamente.')
