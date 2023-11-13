from art import tprint
def menuprincipal():
        tprint("'CATOLICA   NOTICIAS'", font="chunky", chr_ignore=True)
        print('|','-=' * 12, '|')
        print(f'|', ('>'*4), 'MENU PRINCIPAL', ('<'*4), '|')
        print('|','-=' * 12,'|')
        print('| -> [1] CADASTRO ADM      |')
        print('| -> [2] CADASTRO LEITOR   |')
        print('| -> [3] EFETUAR LOGIN     |')
        print('| -> [4] SAIR              |')
        print('-='*13,'|')
        op = input('---> Digite a sua opção: ')

        if op.isdigit():
            op = int(op)
            if op >= 1 and op <= 3:
                return op
            elif op == 4:
                return op
            else:
                print('Opção Inválida! Escolha uma opção de 1 a 4.')

        else:
            print('Opção Inválida! Não aceitamos campo em branco e nem letras alfabeticas.\n'
                  '    ---> Por favor digite os valores conforme o "MENU". <---')

def login(dicionario, login, senha):
    tipo = 0
    pessoa = 0

    for pessoa in dicionario:
        if pessoa["login"] == login and pessoa["senha"] == senha:
            tipo = pessoa["ID"]
    return tipo