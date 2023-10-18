print('{:=^90}'.format(' NOTICIAS QUENTES DA CATOLICA '))
print()

op = 0
usuarios = {}
noticias = {}
jornal = {"publicacoes": []}
while True:
    print('{:=^40}'.format(' MENÚ PRINCIPAL '))
    print('''    [1] CADASTRO ADM
    [2] CADASTRO LEITOR
    [3] EFETUAR LOGIN
    [4] SAIR''')
    op= int(input('Digite a sua opção: '))
    if op >= 5:
        print('Opçao não reconhecida!')

    elif op == 1:
        print('CADASTRAMENTO DE LOGIN E SENHA ADM')
        print()

        while True:
            nome = input('Digite seu nome: ')
            nomeusuario = input('Cadastre o seu login: ')
            senha = input('Cadastre a sua senha: ')
            usuarios[nomeusuario] = [1, nome, senha]
            # regra para proseguir cadastrando usuários.
            resp = ' '
            while resp not in 'SsNn':
                resp = str(input('Deseja continuar cadastrando? Responda [S/N] '))
            if resp == 'N' or resp == 'n':
                break

    elif op == 2:
        print('CADASTRAMENTO DE LOGIN E SENHA LEITOR')
        print()

        while True:
            nome = input('Digite seu nome: ')
            nomeusuario = input('Cadastre o seu login: ')
            senha = input('Cadastre a sua senha: ')
            usuarios[nomeusuario] = [2, nome, senha]
            # regra para proseguir cadastrando usuários.
            resp = ' '
            while resp not in 'SsNn':
                resp = str(input('Deseja continuar cadastrando? Responda [S/N] '))
            if resp == 'N' or resp == 'n':
                break

    elif op == 3:
        nomeusuario = input('Digite o nome de usuário: ')
        senha = input('Digite a senha: ')
        tipo = 0
        if nomeusuario in usuarios:
            if senha==usuarios[nomeusuario][2]:
                tipo = usuarios[nomeusuario][0]
                print('Parabéns, você está logado!!')
            else:
                print('usuário ou senha inválidos')
        else:
            print('usuário ou senha inválidos')

        if(tipo == 1):
            op = 999
            while True:
                print('[1] PUBLICAR NOTÍCIAS')
                print('[2] EDITAR NOTÍCIAS')
                print('[3] REMOVER NOTICIAS')
                print('[4] SAIR')
                op = int(input('Digite a sua opção'))
                if op >= 5:
                    print('Opção inválida, por favor digite novamente')
                if op == 1:
                    titulo = input('Digite o titulo da noticia: ')
                    texto = input('Digite a noticia: ')
                    id = input('Digite o ID da noticia')
                    noticias[id] = [nomeusuario, titulo, texto]
                    print('Noticia salva com sucesso')
                    print(noticias)
                elif op == 4:
                    break
        elif(tipo == 2):
            op = 99
            while True:
                print('[1} LISTAR PUBLICAÇÕES')
                print('[2] LER UMA PUBLICAÇÃO')
                print('[3] ADICIONAR COMENTARIO')
                print('[4] SAIR')
                op = int(input('digite a opcao desejada'))
                if op >= 4:
                    print('Opção inválida, por favor digite novamente!')
                if (op == 1):
                    busca = input('digite o termo presente na noticia')
                    for i in noticias:
                        if (busca in noticias[i][1] or busca in noticias[i][2]):
                            print(f'ID noticia:{i}')
                            print('titulo: ' + noticias[i][1])
                            print('Texto: ' + noticias[i][2])
                            print('-------------*****------------')
                elif (op == 2):
                    comentatio = input('Deixe o seu comentario: ')

                elif (op == 3):
                    curtir = input('Voce curtiu a notícia? [S/N]: ')
                elif op == 4:
                    break
    elif op == 4:
        break
print('<>'*30)
print('Fim do programa!')




