from datetime import datetime
import geral
def cadastrarAdm(usuarios_lista):
    print()
    print('** CADASTRAMENTO DE LOGIN E SENHA JORNALISTA **')
    print()
    while True:
        nome = input('--> Digite seu nome ou digite [0] para "MENÚ PRINCIPAL" : ').capitalize()
        if nome == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif nome == '':
            print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
            continue
        loginAdm = input('--> Cadastre o seu login ou digite [0] para "MENÚ PRINCIPAL" :')
        if loginAdm == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        elif loginAdm == '':
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
            login_existe = False              # Verificar se o login já existe na lista
            for usuario in usuarios_lista:
                if usuario["login"] == loginAdm:
                    print('Login já existe.')
                    login_existe = True
                    break
            if not login_existe:
                DicionarioUsuarioAdm = {"ID": 1, "login": loginAdm, "senha": senha, "nome": nome}
                usuarios_lista.append(DicionarioUsuarioAdm)
                print('Usuario cadastrado com sucesso!')
                break


def exibirMenuAdm(usuariolista, dicionarioUsuario, dicionarioNoticia):

    while True:
        print()
        print('|','-=' * 12, '|')
        print(f'| >>> MENÚ JORNALISTA <<<  |')
        print('|','-=' * 12,'|')
        print('| -> [1] PUBLICAR NOTÍCIAS |')
        print('| -> [2] EDITAR NOTÍCIAS   |')
        print('| -> [3] REMOVER NOTÍCIAS  |')
        print('| -> [4] LISTAR LEITORES   |')
        print('| -> [5] LISTAR COMENTARIOS|')
        print('| -> [6] LISTAR NOTICIAS   |')
        print('| -> [7] SAIR              |')
        print('-='*13,'|')

        op = input('---> Digite a sua opção: ')
        if op.isdigit():
            op = int(op)
            if op == 1:
                criarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 2:
                editarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 3:
                deletarNoticia(dicionarioUsuario, dicionarioNoticia)
            elif op == 4:
                listarleitores(usuariolista, 2)
            elif op == 5:
                listarComentarios(dicionarioUsuario, dicionarioNoticia)
            elif op == 6:
                listarNoticiass(dicionarioUsuario, dicionarioNoticia)
            elif op == 7:
                break
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 6.')

        else:
            print('Opção Inválida! Não aceitamos campo em branco e nem letras alfabeticas.\n'
                  '    ---> Por favor digite os valores conforme o "MENU". <---')



def criarNoticia(dicionarioUsuario, dicionarioNoticia):
    while True:
        titulo = input('Digite o título da notícia ou digite [0] para "MENÚ ADMINISTRADOR" : ').capitalize()
        if titulo == '0':
            print('Cadastro cancelado pelo usuário!')
            break
        if titulo == '':
            print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
            continue
        else:
            conteudo = input('Digite o conteúdo da notícia ou digite [0] para "MENÚ ADMINISTRADOR" : ').capitalize()
            if conteudo == '0':
                print('Cadastro cancelado pelo usuário!')
                break
            if conteudo == '':
                print('Opção Inválida! Não aceitamos campo em branco. Por esse motivo vamos tenta novamente.')
                continue
        # Confirmando que dicionarioUsuario é o nome de usuário
        nome_usuario = dicionarioUsuario

        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": [], "usuario": nome_usuario}
        dicionarioNoticia["publicacoes"].append(nova_publicacao)

        print('Notícia publicada com sucesso.')

        resp = input('Deseja adicionar outra publicação? Digite [S] para Sim ou [N] para Não: ')

        while resp.lower() not in ['s', 'n']:
            print('Opção inválida! Digite [S] para Sim ou [N] para Não.')
            resp = input('Deseja adicionar outra publicação? Digite [S] para Sim ou [N] para Não: ')
        if resp.lower() == 'n':
           break


def editarNoticia(dicionarioUsuario, dicionarioNoticia):

    listnews = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]

    # Codigo para verificar se o usuário não está presente em nenhuma notícia
    if dicionarioUsuario not in [noticia.get("usuario") for noticia in dicionarioNoticia["publicacoes"]]:
        print(f'Olá {dicionarioUsuario}. Ao verificar meu banco de dados, observei que não há nenhuma'
              f' notícia publicada.\nVamos encaminhá-lo para que você possa publicar a sua primeira notícia.')
        print()
        criarNoticia(dicionarioUsuario, dicionarioNoticia)
        return

    print('Lista de noticias:\n--------------------')
    for i, publicacao in enumerate(listnews):
        print(f'ID - {i+1}\nNOTICIA - {publicacao["titulo"]}\nPUBLICAÇÃO - {publicacao["conteudo"]}\n----------------')

    print()
    while True:
        print('Escolha a publicação que deseja editar:')
        for i, publicacao in enumerate(listnews):
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
            print('Cadastro cancelado pelo usuário!')
            break
def deletarNoticia(dicionarioUsuario, dicionarioNoticia):

    listnews = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]
    while True:
        numeroPublicacao = len(listnews)
        if numeroPublicacao == 0:
            print(f'{dicionarioUsuario} não tem notícias para deletar.')
            break

        for i, publicacao in enumerate(listnews, start=1):
            print(f'{i}. {publicacao["titulo"]}')

        escolha = int(input('Digite o número da notícia que deseja deletar (ou 0 para cancelar): '))

        if escolha == 0:
            print('Operação de remoção de notícia cancelada.')
            break

        if 1 <= escolha <= numeroPublicacao:
            confirmacao = input('Tem certeza de que deseja remover esta notícia? (S/N): ')
            if confirmacao == 's' or confirmacao == 'S':
                publicacao = dicionarioNoticia["publicacoes"].pop(dicionarioNoticia["publicacoes"].index(listnews[escolha-1]))
                print(f'A notícia "{publicacao["titulo"]}" foi removida com sucesso.')

            else:
                print('A remoção da notícia foi cancelada pelo usuário.')
            break
        else:
            print('Número de notícia inválido. Tente novamente.')
def listarleitores(dicionarioLeitores, idLeitor):
    for leitor in dicionarioLeitores:
        if leitor.get('ID') == idLeitor:
            print('Lista de Leitores:')
            print(f"Nome: {leitor['nome']}")
            print(f"Login: {leitor['login']}")
            return

    print(f"Usuário com ID {idLeitor} não encontrado.")


def listarComentarios(dicionarioUsuario, dicionarioNoticia):
    listnews = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]

    print('\nLISTA DE COMENTÁRIOS\n')
    for i, noticia in enumerate(listnews, start=1):
        print(f'{i}ª noticia\nTítulo: {noticia["titulo"]}')
        if noticia["comentarios"]:
            print('Comentários:')
            for j, comentario in enumerate(noticia["comentarios"], start=1):
                print(f'{j}º comentário- {comentario["leitor"]}: {comentario["comentario"]}\n')
        else:
            print('Sem comentários.\n')


def listarNoticiass(dicionarioUsuario, dicionarioNoticia):
    hoje = datetime.now()

    # Linha para pegar a noticia no dicionarioNoticia pertence a pessoa logada
    listnews = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]

    # reconhecer se tem alguma noticia no Usuário logado e fazer uma busca no dicionario para
    # para saber se tem noticia
    if dicionarioUsuario not in [noticia.get("usuario") for noticia in dicionarioNoticia["publicacoes"]]:
        print(f'Olá {dicionarioUsuario}. Ao verificar meu banco de dados, observei que não há nenhuma'
              f' notícia publicada.\nVamos encaminhá-lo para que você possa publicar a sua primeira notícia.')
        print()
        criarNoticia(dicionarioUsuario, dicionarioNoticia)  # Sera encaminhado para a função cadastrar noticia
        return

    for i, v in enumerate(listnews):
        print(f'{i+1}ª noticia\nTitulo: {v["titulo"]}\nConteudo: {v["conteudo"]}\nEscritor: {dicionarioUsuario}'
              f'\nData da publicação: {hoje.date()}')