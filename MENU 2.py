'''filme = {'titulo':'Star Wars', 'ano': 1977, 'diretor':'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())'''

'''pessoas = {'nome':'gustavo','sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])'''


def fazer_login(adms_cadastrados):
    nome_login = input('Digite o seu login: ')
    senha_login = input('Digite a sua senha: ')

    if nome_login in adms_cadastrados and adms_cadastrados[nome_login] == senha_login:
        print('Parabéns, você está logado!!')
    else:
        print('Usuário e/ou senha incorretos.')

# Exemplo de adms cadastrados em um dicionário
adms_cadastrados = {
    'admin1': 'senha123',
    'admin2': 'senha456'
}

fazer_login(adms_cadastrados)


# Crie um dicionário vazio
meu_dicionario = {}

# Adicione um par chave-valor ao dicionário
meu_dicionario['chave1'] = 'valor1'

# Você também pode adicionar múltiplos pares chave-valor de uma vez
meu_dicionario['chave2'] = 'valor2'
meu_dicionario['chave3'] = 'valor3'

# O dicionário agora contém três pares chave-valor
print(meu_dicionario)



adms_cadastrados = {}  # Crie um dicionário vazio para armazenar os adms

while True:
    op = int(input("Escolha a opção (1 para cadastrar ADM, 2 para sair): ")

    if op == 1:
        print()
        print('PREENCHA O CADASTRO ADM')
        print()
        Login = input('Cadastre o seu login: ')
        Senha = input('Cadastre a sua senha: ')
        adms_cadastrados[Login] = Senha  # Adicione o novo ADM ao dicionário

    elif op == 2:
        break  # Sair do loop

    else:
        print("Opção inválida. Tente novamente.")

print("Adms cadastrados:", adms_cadastrados)
