from fpdf import FPDF
import textwrap
import os
import pyttsx3
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
                DicionarioUsuarioAdm = {"ID": 1, "login": loginAdm, "senha": senha, "nome": nome,}
                usuarios_lista.append(DicionarioUsuarioAdm)
                print('Usuario cadastrado com sucesso!')
                break


def exibirMenuAdm(usuariolista, dicionarioUsuario, dicionarioNoticia):

    while True:

        print('''
| -=-=-=-=-=-=-=-=-=-=-=-=-=  |
|  >>>> MENÚ JORNALISTA <<<<  |

| -> [1] PUBLICAR NOTÍCIAS    |
| -> [2] EDITAR NOTÍCIAS      |
| -> [3] REMOVER NOTÍCIAS     |
| -> [4] LISTAR LEITORES      |
| -> [5] LISTAR COMENTARIOS   |
| -> [6] LISTAR NOTICIAS      |
| -> [7] TOP NOTÍCIAS POR ADM |
| -> [8] TOP NOTÍCIAS GERAL   |
| -> [9] BAIXAR NOTÍCIAS .TXT |
| -> [10] SAIR                |
| -=-=-=-=-=-=-=-=-=-=-=-=-=  |''')

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
                mostrar_usuarios_com_id_2(usuariolista)
            elif op == 5:
                listarComentarios(dicionarioUsuario, dicionarioNoticia)
            elif op == 6:
                listarNoticiass(dicionarioUsuario, dicionarioNoticia)
            elif op == 7:
                top_noticias_adm_ordenadas = top_noticias_adm(dicionarioNoticia, dicionarioUsuario)
                print("Top Notícias Mais Curtidas:")
                for i, publicacao in enumerate(top_noticias_adm_ordenadas, start=1):
                    print(f"{i}. Título: {publicacao['titulo']} - Curtidas: {publicacao.get('curtida', 0)}")
                print()
            elif op == 8:
                top_noticias_geral_ordenadas = top_noticias_geral(dicionarioNoticia)
                print("Top Notícias Mais Curtidas (Geral):")
                for i, publicacao in enumerate(top_noticias_geral_ordenadas, start=1):
                    print(f"{i}. Título: {publicacao['titulo']}\nEscritor: {publicacao['usuario']}\nCurtidas: {publicacao.get('curtida', 0)}")
                print()

            elif op == 9:
                while True:
                    print('''
| -=-=-=-=-=-=-=-=-=-=-=-=-=  |
|  >>>> MENÚ DOWNLOAD's <<<<  |

| -> [1] BAIXAR NOTÍCIAS EM TXT    |
| -> [2] BAIXAR NOTÍCIAS EM PDF    |
| -> [3] VOLTAR P/ MENU JORNALISTA |
| -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= |''')

                    op = int(input('Digite a opção desejada: '))
                    if op == 1:
                        baixarnoticias(dicionarioUsuario, dicionarioNoticia)
                    elif op == 2:
                        noticias_a_salvar = [noticia for noticia in dicionarioNoticia["publicacoes"] if
                                             noticia.get("usuario") == dicionarioUsuario]
                        text_to_pdf(f"Noticias de {dicionarioUsuario}.pdf", noticias_a_salvar)
                        print('Arquivo PDF baixado com sucesso!')
                    elif op == 3:
                        break
                    break


            elif op == 10:
                break
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 10')

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

        # Gerando numero de ID para cada noticia
        id = len(dicionarioNoticia["publicacoes"]) + 1

        # Obtendo a data e hora atuais
        data_publicacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": [], "usuario": nome_usuario,
                           "curtida": 0, "ID": id, "data_publicacao": data_publicacao}
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
def mostrar_usuarios_com_id_2(usuarios_lista):
    usuarios_com_id_2 = [usuario for usuario in usuarios_lista if usuario.get('ID') == 2]

    if usuarios_com_id_2:
        print("Lista de Leitores:")
        print()
        for usuario in usuarios_com_id_2:
            print(f"Nome: {usuario['nome']}\nLogin: {usuario['login']}")
            print()
    else:
        print("Nenhum usuário encontrado.")



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
        data_publicacao = hoje.strftime("%d/%m/%Y")  # Formatar a data no estilo brasileiro
        print(f'{i + 1}ª notícia\nTítulo: {v["titulo"]}\nConteúdo: {v["conteudo"]}\nEscritor: {dicionarioUsuario}'
              f'\nData da publicação: {data_publicacao}')


def curtirNoticia(dicionarioUsuario, DicionarioNoticia):

    while True:
        print('Você gostou da matéria que acabou de ler?')
        resposta = input('Digite [S] para Sim e [N] para Não').lower()

        if resposta == 'S':
            while True:
                numero_noticia = input("Digite o número da notícia que você gostou (ou 0 para cancelar): ")
                if numero_noticia.isdigit():
                    numero_noticia = int(numero_noticia)
                    if 1 <= numero_noticia <= len(DicionarioNoticia["publicacoes"]):
                        DicionarioNoticia["publicacoes"][numero_noticia - 1].setdefault('curtida', 0)
                        DicionarioNoticia["publicacoes"][numero_noticia - 1]["curtida"] += 1
                        print("Você curtiu esta notícia!")
                        break
                    else:
                        print("Número de notícia inválido. Tente novamente.")
                elif numero_noticia == 0:
                    break
                else:
                    print("Por favor, digite um número válido ou 0 para cancelar.")



def top_noticias_adm(dicionarioNoticia, usuario_atual):
    publicacoes_adm = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == usuario_atual]
    publicacoes_ordenadas = sorted(publicacoes_adm, key=lambda x: x.get("curtida", 0), reverse=True)
    return publicacoes_ordenadas


def top_noticias_geral(dicionarioNoticia):
    publicacoes_adm = [noticia for noticia in dicionarioNoticia["publicacoes"] if "curtida" in noticia]
    publicacoes_ordenadas = sorted(publicacoes_adm, key=lambda x: x.get("curtida", 0), reverse=True)
    return publicacoes_ordenadas


def baixarnoticias(dicionarioUsuario, dicionarioNoticia):
   publicacoes_adm = [noticia for noticia in dicionarioNoticia["publicacoes"] if noticia.get("usuario") == dicionarioUsuario]
   with open(f"Noticias de {dicionarioUsuario}.txt", "w") as arquivo:
       for i in publicacoes_adm:
           arquivo.write(f'ID: {i["ID"]}\nNoticia: {i["titulo"]}\nConteudo: {i["conteudo"]}\nData Publicada: {i["data_publicacao"]}\n\n')
   arquivo.close()
   print('Arquivo TXT baixado com sucesso!')


def text_to_pdf(filename, noticias):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)

    # Concatenando todas as notícias em um único texto
    texto_noticias = ""
    for noticia in noticias:
        texto_noticias += (f'ID da Notícia: {noticia["ID"]}\nEscritor: {noticia["usuario"]}\n'
                           f'Título: {noticia["titulo"]}\nConteúdo: {noticia["conteudo"]}\nData da publicação: {noticia["data_publicacao"]}\n'
                           f'Comentarios: {noticia["comentarios"]}\n\n')

    # separando o texto em uma lista de strings a partir de cada quebra de linha
    splitted = texto_noticias.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)
        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')
