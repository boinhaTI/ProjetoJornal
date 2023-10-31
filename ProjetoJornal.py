import menuAdm
import geral
import leitor
from art import tprint

tprint("CATOLICA   NOTICIAS'", font="chunky", chr_ignore=True)

op = 0
usuarios_lista = []
jornal = {"publicacoes": []}

# programa principal
while True:

    op = geral.menuprincipal()

    if op >= 5:
        print('Opção Inválida!')

    if op == 1:
        menuAdm.cadastrarAdm(usuarios_lista)
    elif op == 2:
        leitor.cadastrarLeitor(usuarios_lista)

    elif op == 3:
        nomeusuario = input('Digite o login: ')
        senha = input('Digite a senha: ')

        tipo = geral.login(usuarios_lista, nomeusuario, senha)

        if tipo == 1:
            menuAdm.exibirMenuAdm(nomeusuario, jornal)

        elif op == 2:
            menuAdm.editarNoticia(nomeusuario, jornal)

        elif op == 3:
            menuAdm.deletarNoticia(nomeusuario)

        elif op == 4:
            break

        elif tipo == 2:
            leitor.exibirMenuLeitor(nomeusuario, jornal)

        if op == 1:
            leitor.listarNoticia(nomeusuario, jornal)

        elif op == 2:
            leitor.lerPublicacao(nomeusuario, jornal)
        elif op == 3:
            leitor.adicionarComentario(nomeusuario, jornal)
        elif op == 4:
            break


    elif op == 4:
        break
print('<>' * 30)
print('Saindo do jornal!')


