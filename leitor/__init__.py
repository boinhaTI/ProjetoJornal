def cadastrarLeitor(dicionarioUsuario):

    print('CADASTRAMENTO DE LOGIN E SENHA LEITOR')
    print()
    while True:
        nome = input('Digite seu nome ou digite [0] para cancelar: ').capitalize()
        if nome == '0':
            break
        elif nome == '':
            print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
            continue

        loginLeitor = input('--> Cadastre o seu login ou digite [0] para "MENÚ PRINCIPAL" :')
        if loginLeitor == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif loginLeitor == '':
            print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
            continue
        senha = input('--> Cadastre o seu senha ou digite [0] para "MENÚ PRINCIPAL" : ')
        if senha == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif senha == '':
            print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
            continue
        else:
            login_existe = False            # Verificar se o login já existe na lista
            for usuario in dicionarioUsuario:
                if usuario["login"] == loginLeitor:
                    print('Login já existe.')
                    login_existe = True
                    break
            if not login_existe:
                DicionarioUsuarioLeitor = {"ID": 2, "login": loginLeitor, "senha": senha, "nome": nome}
                dicionarioUsuario.append(DicionarioUsuarioLeitor)
                print('Usuario cadastrado com sucesso!')
                break


def exibirMenuLeitor(usuariolista, dicionarioUsuario, DicionarioNoticia):
    print()
    print(f'Seja bem-vindo(a) >>> {dicionarioUsuario} <<<')
    print()

    while True:
        print('|', '-=' * 13, ' |')
        print(f'| >>>>> MENÚ DO LEITOR <<<<<  |')
        print('|', '-=' * 13, ' |')
        print('| -> [1] LISTAR PUBLICAÇÕES   |')
        print('| -> [2] LER UMA PUBLICAÇÃO   |')
        print('| -> [3] ADICIONAR COMENTÁRIO |')
        print('| -> [4] SAIR                 |')
        print('-=' * 14, ' |')

        op = input('---> Digite a sua opção: ')
        if op.isdigit():
            op = int(op)
            if op == 1:
                listarNoticia(dicionarioUsuario, DicionarioNoticia)
            elif op == 2:
                lerPublicacao(dicionarioUsuario, DicionarioNoticia)
            elif op == 3:
                adicionarComentario(dicionarioUsuario, DicionarioNoticia)
            elif op == 4:
                break
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 4.')

        else:
            print('Opção Inválida! Não aceitamos campo em branco e nem letras alfabeticas.\n'
                  '    ---> Por favor digite os valores conforme o "MENU". <---')


def listarNoticia(dicionariousuario, DicionarioNoticia):

    if DicionarioNoticia["publicacoes"]:
        for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
            print(f'{i + 1}. {publicacao["titulo"]}')
            print(f'Autor da  Noticia: {publicacao["usuario"]}\n')
    else:
        print('Não tem nenhuma notícia publicada')


def lerPublicacao(dicionariousuario, DicionarioNoticia):
    while True:
        if DicionarioNoticia["publicacoes"]:
            for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
                print(f'{i + 1}. {publicacao["titulo"]}')

        else:
            print('Não tem nenhuma notícia publicada')

        escolha = int(input('Digite o número da publicação que deseja ler (ou 0 para cancelar): '))

        if escolha == 0:
            break
        if 1 <= escolha <= len(DicionarioNoticia["publicacoes"]):
            publicacao = DicionarioNoticia["publicacoes"][escolha - 1]
            print(f'Noticia: {publicacao.get("titulo", "")}')
            print(publicacao.get("conteudo", ""))

            # Exibir comentários da notícia escolhida
            if publicacao["comentarios"]:
                print('Comentários da noticia escolhida:')
                for i, comentario in enumerate(publicacao["comentarios"], start=1):
                    leitor = comentario.get('leitor', '')
                    comentario_text = comentario.get('comentario', '')
                    print(f' {i}º comentário- {leitor}: {comentario_text}')
            else:
                print('A notícia não possui comentários.')
        break


def adicionarComentario(dicionarioUsuario, DicionarioNoticia):

    if not DicionarioNoticia["publicacoes"]:
        print('Não há notícias publicadas.')
        return
    else:
        while True:
            for i, publicacao in enumerate(DicionarioNoticia["publicacoes"], start=1):
                print(f'{i}. {publicacao["titulo"]} - Autor {publicacao["usuario"]}\n')
            else:
                indice = input('Digite o número da publicação para adicionar um comentário (ou [0] para cancelar): ')

                if indice == '0':
                    break

                try:
                    indice = int(indice)
                except ValueError:
                    print('Número de publicação inválido. Tente novamente.')
                    continue

                if 1 <= indice <= len(DicionarioNoticia["publicacoes"]):
                    publicacao = DicionarioNoticia["publicacoes"][indice - 1]
                    print(f'Título: {publicacao["titulo"]}')
                    print(publicacao["conteudo"])
                    nomeusuario = input('Digite o seu login: ')
                    comentario = input('Digite o seu comentário: ')


                    usuario_encontrado = False
                    if nomeusuario == dicionarioUsuario:
                        usuario_encontrado = True

                    if usuario_encontrado:
                        publicacao["comentarios"].append({"leitor": nomeusuario, "comentario": comentario})
                        print('Comentário adicionado com sucesso.')

                        return
                    else:
                        print('Usuário não encontrado. Comentário não adicionado.')
                else:
                    print('Número de publicação inválido. Tente novamente.')