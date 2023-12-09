from datetime import datetime

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
        print('|', '-=' * 18, '|')
        print(f'| >>>>>>>>>> MENÚ DO LEITOR <<<<<<<<<< |')
        print('|', '-=' * 18, '|')
        print('| -> [1] BUSCAR NOTÍCIAS               |')
        print('| -> [2] LER UMA PUBLICAÇÃO            |')
        print('| -> [3] ADICIONAR COMENTÁRIO E CURTIR |')
        print('| -> [4] LISTA O TOP DAS MAIS CURTIDAS |')
        print('| -> [5] SAIR                          |')
        print('-=' * 18, '|')

        op = input('---> Digite a sua opção: ')
        if op.isdigit():
            op = int(op)
            if op == 1:
                buscarNoticia(dicionarioUsuario, DicionarioNoticia)
            elif op == 2:
                lerPublicacao(dicionarioUsuario, DicionarioNoticia)
            elif op == 3:
                adicionarComentario(dicionarioUsuario, DicionarioNoticia)
            elif op == 4:
                top_noticias_ordenadas = top_noticias(DicionarioNoticia)
                print("Top Notícias Mais Curtidas:")
                for i, publicacao in enumerate(top_noticias_ordenadas, start=1):
                    print(
                        f"{i}ª-> Notícia: {publicacao['titulo']} - Autor: {publicacao['usuario']} - Curtidas: {publicacao['curtida']}")
            elif op == 5:
                break
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 4.')

        else:
            print('Opção Inválida! Não aceitamos campo em branco e nem letras alfabeticas.\n'
                  '    ---> Por favor digite os valores conforme o "MENU". <---')


def buscarNoticia(dicionariousuario, DicionarioNoticia):

    palavraChave = input('Digite uma palavra CHAVE de busca ou ENTER para listar todas: ')
    print()
    noticiaEncontrada = False

    for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
        if palavraChave in publicacao["titulo"] or palavraChave in publicacao["conteudo"]:
            noticiaEncontrada = True
            print(f'{i+1}. {publicacao["titulo"]}')
            print(f'Autor da notícia: {publicacao["usuario"]}\n')
    if not noticiaEncontrada:
        print('Não foram encontradas notícias com essa palavra-chave')


def lerPublicacao(dicionariousuario, DicionarioNoticia):

    while True:
        if DicionarioNoticia["publicacoes"]:
            for i, publicacao in enumerate(DicionarioNoticia["publicacoes"]):
                print(f'{i + 1}. {publicacao["titulo"]}')
        else:
            print('Não tem nenhuma notícia publicada')
            break

        escolha = input('Digite o número da publicação que deseja ler (ou 0 para cancelar): ')
        print()
        if escolha.isdigit():
            escolha = int(escolha)
        if escolha == 0:
            break
        elif escolha == '':
            print('Opção Inválida! Não aceitamos campo em branco')
        else:
            if 1 <= escolha <= len(DicionarioNoticia["publicacoes"]):
                publicacao = DicionarioNoticia["publicacoes"][escolha - 1]
                print(f'Noticia: {publicacao.get("titulo", "")}')
                print(f'Conteudo:{publicacao.get("conteudo", "")}')
                print()

                # Exibir comentários da notícia escolhida
                if publicacao["comentarios"]:
                    print('Comentários da noticia escolhida:')
                    for i, comentario in enumerate(publicacao["comentarios"], start=1):
                        leitor = comentario.get('leitor', '')
                        comentario_text = comentario.get('comentario', '')
                        print(f' {i}º comentário - {leitor}: {comentario_text}')

                else:
                    print('A notícia não possui comentários.')
            break



def adicionarComentario(dicionarioUsuario, DicionarioNoticia):
    print(DicionarioNoticia)
    if not DicionarioNoticia["publicacoes"]:
        print('Não há notícias publicadas.')
        return
    else:
        # Iterar sobre as publicações
        for publicacao in DicionarioNoticia["publicacoes"]:
            # Adicionar o campo "curtidas" para cada publicação, se não existir
            if "curtidas" not in publicacao:
                publicacao["curtidas"] = []  # mostrarar quais os logins que curtiram as noticias

        while True:
            for i, publicacao in enumerate(DicionarioNoticia["publicacoes"], start=1):
                print(
                    f'{i}. {publicacao["titulo"]}\nEscritor {publicacao["usuario"]}')

            indice = input('Digite o número da publicação para interagir ou [0] para cancelar: ')

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

                escolha = input('Digite [C] para comentar, [L] para curtir ou [0] para cancelar: ')

                if escolha.upper() == 'C':
                    nomeusuario = input('Digite o seu login: ')
                    comentario = input('Digite o seu comentário: ')

                    usuario_encontrado = False
                    if nomeusuario == dicionarioUsuario:
                        usuario_encontrado = True

                    if usuario_encontrado:
                        publicacao["comentarios"].append({"leitor": nomeusuario, "comentario": comentario})
                        print('Comentário adicionado com sucesso.')
                        break

                    else:
                        print('Usuário não encontrado. Comentário não adicionado.')

                if escolha.upper() == 'L':
                    if dicionarioUsuario in publicacao["curtidas"]:
                        print('Você já deu like nesta notícia.')
                    else:
                        publicacao["curtidas"].append(dicionarioUsuario)
                        publicacao["curtida"] += 1
                        print('Notícia curtida com sucesso.')
                        break
                elif escolha == '0':
                    break
                else:
                    print('Opção inválida.')

            else:
                print('Número de publicação inválido. Tente novamente.')


def top_noticias(dicionario_noticia):
    publicacoes = dicionario_noticia.get("publicacoes", [])
    publicacoes_ordenadas = sorted(publicacoes, key=lambda x: x.get("curtida", 0), reverse=True)
    return publicacoes_ordenadas

# # Obtendo o top das mais curtidas
# top_noticias_ordenadas = top_noticias(dicionario_noticia)
#
# # Exibindo o top das mais curtidas
# for i, publicacao in enumerate(top_noticias_ordenadas, start=1):
#     print(f"{i}. {publicacao['titulo']} - Autor: {publicacao['usuario']} - Curtidas: {publicacao['curtida']}")