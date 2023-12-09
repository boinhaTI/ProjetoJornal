'''
f = open('nomes.txt', 'a')
f.write('\nmeu dia de ganhar')
f.close()


'''


def salvarArquivo(texto, login):

    f = open(f'produtos_{login}.txt', 'w')
    f.write(texto)
    f.close()


def salvarprodutos():
    lista = []
    lista.append({'nome': 'lapis', 'valor': 14, 'qtde': 5})
    lista.append({'nome': 'cpu', 'valor': 2000, 'qtde': 2})

    for p in lista:
        nome = p['nome']
        valor = p['valor']
        qtde = p['qtde']

        texto = f'nome do produto: {nome}\n'
        texto = texto + f'valor do produto: {valor}\n'
        texto = texto + f'qtde do produto: {qtde}\n\n'

        salvarArquivo(texto, 'rene')


def lerarquivo():
    f = open('nomes.txt', 'r')

    nomes = {}

    for linha in f.readlines():

        nomes[linha.split(':')[0]] = float(linha.split(':')[1].replace('\n','').replace(',','.'))

    f.close()
    print(nomes)

salvarprodutos()i