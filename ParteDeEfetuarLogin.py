# Dicionário para armazenar as publicações
jornal = {"publicacoes": []}



while True:
    print("\nEscolha uma ação:")
    print("1. Publicar notícia (somente adm)")
    print("2. Listar publicações")
    print("3. Ler uma publicação")
    print("4. Adicionar comentário")
    print("5. Sair")
    escolha = int(input("Digite o número da ação desejada: "))
    if escolha >= 6:
        print('Opção Inválida!')
    if escolha == 1:
        titulo = input("Digite o título da notícia: ")
        conteudo = input("Digite o conteúdo da notícia: ")
        nova_publicacao = {"titulo": titulo, "conteudo": conteudo, "comentarios": []}
        jornal["publicacoes"].append(nova_publicacao)
        print("Notícia publicada com sucesso.")