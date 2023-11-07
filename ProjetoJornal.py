import menuAdm
import geral
import leitor
from art import tprint

tprint("CATOLICA   NOTICIAS'", font="chunky", chr_ignore=True)

op = 0
usuarios_lista = []
jornal = {"publicacoes": []}

while True:
    print()
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
                menuAdm.exibirMenuAdm(nomeusuario, jornal)

            elif tipo == 2:
                leitor.exibirMenuLeitor(usuarios_lista, jornal)

            else:
                print('Opção invalida!')
    elif op == 4:
        break

print('<>' * 30)
print('Saindo do jornal!')