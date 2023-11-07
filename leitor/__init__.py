def cadastrarLeitor(dicionarioUsuario):
    print('CADASTRAMENTO DE LOGIN E SENHA LEITOR')
    print()
    while True:
        nome = input('Digite seu nome ou digite [0] para cancelar: ')
        if nome == '0':
            break
        loginLeitor = input('Cadastre o seu login: ')
        senha = input('Cadastre a sua senha: ')

        # Verificar se o login já existe na lista

        login_existe = False
        for usuario in dicionarioUsuario:
            if usuario["login"] == loginLeitor:
                print('Login já existe.')
                login_existe = True
                break
        if not login_existe:
            DicionarioUsuarioLeitor = {"ID": 2, "login": loginLeitor, "senha": senha}
            dicionarioUsuario.append(DicionarioUsuarioLeitor)
            print('Usuario cadastrado com sucesso!')
            break

        resp = ' '
        while resp not in 'SsNn':
            resp = input('Deseja continuar cadastrando? Responda [S/N] ')
        if resp.lower() == 'n':
            break

def exibirMenuLeitor(dicionarioUsuario, DicionarioNoticia):
    while True:
        print('[1] LISTAR PUBLICAÇÕES')
        print('[2] LER UMA PUBLICAÇÃO')
        print('[3] ADICIONAR COMENTÁRIO')
        print('[4] SAIR')
        op = int(input('Digite a sua opção: '))

        if op == 1:
            listarNoticia(dicionarioUsuario, DicionarioNoticia)
        elif op == 2:
            lerPublicacao(dicionarioUsuario, DicionarioNoticia)
        elif op == 3:
            adicionarComentario(dicionarioUsuario, DicionarioNoticia)
        elif op == 4:
            break


def listarNoticia(dicionariousuario, DicionarioNoticia):
    for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
        print(f'{i + 1}. {publicacao["titulo"]}')


def lerPublicacao(dicionariousuario, DicionarioNoticia):

    print('Digite o número da publicação que deseja ler (ou 0 para cancelar): ')
    indice = int(input())
    if indice == 0:
        return
    if 1 <= indice <= len(DicionarioNoticia["publicacoes"]):
        publicacao = DicionarioNoticia["publicacoes"][indice - 1]
        print(f'Título: {publicacao["titulo"]}')
        print(publicacao["conteudo"])
        print('\nComentários:')

        for i, comentario in enumerate(publicacao["comentarios"], start=1):
            leitor = comentario["leitor"]
            comentario_text = comentario["comentario"]

            #Encontrar o usuário pelo login em usuarios_lista
            leitorEncontrado = False
            for usuario in dicionariousuario:
                if usuario["login"] == leitor:
                    user_found = True
                    leitor_nome = usuario["login"]
                    print(f'{i}. {leitor_nome}: {comentario_text}')
                    break



    else:
        print('Número de publicação inválido. Tente novamente.')


def adicionarComentario(dicionarioUsuario, DicionarioNoticia):

    indice = int(input('Digite o número da publicação para adicionar um comentário (ou [0] para cancelar): '))

    indice = int(indice)
    if indice == 0:
        return
    if 1 <= indice <= len(DicionarioNoticia["publicacoes"]):
        publicacao = DicionarioNoticia["publicacoes"][indice - 1]
        print(f'Título: {publicacao["titulo"]}')
        print(publicacao["conteudo"])
        nomeusuario = input('Digite o seu login: ')
        comentario = input('Digite o seu comentário: ')

        # Checar se o usuarios existe na lista usuario_lista
        usuario_encontrado = False
        for usuario in dicionarioUsuario:
            if usuario["login"] == nomeusuario:
                usuario_encontrado = True

        if usuario_encontrado:
            publicacao["comentarios"].append({"leitor": nomeusuario, "comentario": comentario})
            print('Comentário adicionado com sucesso.')
            return
        else:
            print('Usuário não encontrado. Comentário não adicionado.')
    else:
        print('Número de publicação inválido. Tente novamente.')
