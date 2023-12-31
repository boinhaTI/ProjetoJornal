import menuAdm
import geral
import leitor
from art import tprint
from datetime import datetime
tprint("CATOLICA   NOTICIAS'", font="chunky", chr_ignore=True)


op = 0
usuarios_lista = [{'ID': 1, 'login': 'boinha', 'senha': '123', 'nome': 'Cristofer'},
                  {'ID': 2, 'login': 'edilane', 'senha': '123', 'nome': 'Edilane'}]
jornal = {'publicacoes': []}


while True:

    op = geral.menuprincipal()

    if op == 1:
        menuAdm.cadastrarAdm(usuarios_lista)
    elif op == 2:
        leitor.cadastrarLeitor(usuarios_lista)

    elif op == 3:
        while True:
            nomeusuario = input('Digite o login ou digite [0] para cancelar: ')
            if nomeusuario == "0":
                print('Opção cancela pelo usuario.')
                break
            senha = input('Digite a senha: ')

            tipo = geral.login(usuarios_lista, nomeusuario, senha)

            if tipo == 1:
                menuAdm.exibirMenuAdm(usuarios_lista, nomeusuario, jornal)
                break
            elif tipo == 2:
                leitor.exibirMenuLeitor(usuarios_lista,nomeusuario, jornal)
                break
            elif nomeusuario == '' or senha == '':
                print('O campo login ou senha esta em branco!')
            else:
                print('ERRO! Login ou senha incorreto!')
    elif op == 4:
        break

print('<>' * 30)
print('Saindo do jornal!')