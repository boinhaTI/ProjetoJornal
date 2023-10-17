adms_cadastrados = {}
usuarios_cadastrados = []
noticias = []

def inserir_noticia():
    titulo = input('Digite o título da notícia: ')
    conteudo = input('Digite o conteúdo da notícia: ')
    noticias.append({'titulo': titulo, 'conteudo': conteudo})
    print('Notícia inserida com sucesso!')

def listar_noticias():
    if noticias:
        print('Notícias:')
        for idx, noticia in enumerate(noticias, start=1):
            print(f'{idx}. Título: {noticia["titulo"]}')
            print(f'   Conteúdo: {noticia["conteudo"]}')
    else:
        print('Nenhuma notícia disponível.')

while True:
    print('[1] CADASTRO ADM
[2] CADASTRO USUÁRIO
[3] EFETUAR LOGIN
[4] INSERIR NOTÍCIA
[5] LISTAR NOTÍCIAS
[6] SAIR')
    op = int(input('Digite a sua opção: '))

    if op == 1:
        # Código de cadastro de ADM

    elif op == 2:
        # Código de cadastro de usuário

    elif op == 3:
        # Código de login

    elif op == 4:
        if usuario_logado:  # Certifique-se de ter uma variável de controle para o usuário logado
            inserir_noticia()
        else:
            print('Você precisa estar logado como ADM ou usuário para inserir notícias.')

    elif op == 5:
        listar_noticias()

    elif op == 6:
        break

    else:
        print('Opção inválida. Tente novamente.')

print('Adms cadastrados:', adms_cadastrados)
print('Usuários cadastrados:', usuarios_cadastrados)









usuario_logado = False  # Variável de controle para rastrear o login do usuário

adms_cadastrados = {}
usuarios_cadastrados = {}
noticias = {}

# Definições de funções (cadastro, login, inserir_noticia, listar_noticias)

while True:
    print('''[1] CADASTRO ADM
[2] CADASTRO USUÁRIO
[3] EFETUAR LOGIN
[4] INSERIR NOTÍCIA
[5] LISTAR NOTÍCIAS
[6] SAIR'')

    op = int(input('Digite a sua opção: ')

    if op == 1:
        # Código de cadastro de ADM

    elif op == 2:
        # Código de cadastro de usuário

    elif op == 3:
        # Código de login
        usuario_logado = True  # Marcar o usuário como logado

    elif op == 4:
        if usuario_logado:
            inserir_noticia()
        else:
            print('Você precisa estar logado como ADM ou usuário para inserir notícias.')

    elif op == 5:
        listar_noticias()

    elif op == 6:
        break

    else:
        print('Opção inválida. Tente novamente.')

    if usuario_logado:  # Bloco para usuário logado
        print('\n[7] NOVO MENU PARA USUÁRIO LOGADO')
        op_usuario_logado = int(input('Escolha uma opção: ')

        if op_usuario_logado == 7:
            print('Opção do menu para usuário logado')

print('Adms cadastrados:', adms_cadastrados)
print('Usuários cadastrados:', usuarios_cadastrados)

