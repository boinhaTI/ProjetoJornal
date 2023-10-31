def menuprincipal():

    print('==== MENU PRINCIPAL ====')
    print('[1] CADASTRO ADM')
    print('[2] CADASTRO LEITOR')
    print('[3] EFETUAR LOGIN')
    print('[4] SAIR')
    op = int(input('Digite a sua opção: '))

    if op >= 5:
        print('Opção Inválida!')
    return op


def login(dicionario, login, senha):
    tipo = 0
    pessoa = 0

    for pessoa in dicionario:
        if pessoa["login"] == login and pessoa["senha"] == senha:
            tipo = pessoa["ID"]
    return tipo