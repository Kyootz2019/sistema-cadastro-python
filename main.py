def add_contatos():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    
    arquivo = open("Contatos.txt", "a")
    arquivo.write(nome + " - " + telefone + "\n")
    arquivo.close()

def ver_contatos():
    try:
        with open("Contatos.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())
                print("------------------")
    except FileNotFoundError:
        print("Nenhum contato cadastrado ainda.")

def buscar_contato():
    arquivo = open("Contatos.txt","r")
    buscar = input("Digite um nome para buscar: ").strip().lower()
    encontrado = False
    
    for linha in arquivo:
        if buscar in linha.lower():
            print(linha.strip())
            encontrado = True
            break
    if encontrado == False:
        print("Contato não encontrado.")
    arquivo.close()
def remover_contato():
    nome = input("Qual contato deseja remover: ").lower().strip()
    arquivo = open("Contatos.txt", "r")
    nova_lista = []
    encontrado = False
    
    for linha in arquivo:
        if nome in linha.lower():
            encontrado = True
        else:    
            nova_lista.append(linha)
    
    arquivo.close()
    
    arquivo = open("Contatos.txt", "w")
    for linha in nova_lista:
        arquivo.write(linha)
    arquivo.close()

    if encontrado:
        print("Contato removido.")
    else:
        print("Contato não encontrado.")

def editar_contato():
    editar_nome = input("Nome para editar: ").lower().strip()
    arquivo = open("Contatos.txt", "r")
    nova_lista = []
    encontrado = False
    
    for linha in arquivo:
        #percorre cada contato do arquivo
        if editar_nome in linha.lower():
            #verifica se o nome digitado está nessa linha
            print("""
1 - Alterar nome
2 - Alterar telefone
""")
            opcao = input("Escolha a opção: ")

            nome, telefone = linha.strip().split(" - ")
            #.split() -> ele quebra o texto onde tiver " - ", virando [" "," "]
            #
            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                linha_nova = novo_nome + " - " + telefone + "\n"
                #troca só o nome e mantém telefone
            
            elif opcao == "2":
                novo_telefone = input("Digite o novo telefone: ")
                linha_nova = nome + " - " + novo_telefone + "\n"
                #troca só o telefone e mantém nome

            nova_lista.append(linha_nova)
            #Adiciona o contato editado na lista
            encontrado = True
            break
        else:
            nova_lista.append(linha)
            #Se nao for contato mantém ele igual
    arquivo.close()
    #fecha o arquivo
    arquivo = open("Contatos.txt", "w")
    #abre ele em modo de escrita(apaga tudo)
    for linha in nova_lista:
        arquivo.write(linha)
        #reescreve tudo atualizado
    arquivo.close()
    #fecha o arquivo
    if encontrado:
        print("contato editado.")
    
    else:
        print("Contato não encontrado.")

while True:
    print("""
1 - Adicionar contatos
2 - Ver contatos
3 - Buscar contato
4 - Remover contato
5 - Editar contatos
6 - sair
""")

    opcao = input("Escolha uma opção: ") 

    if opcao == "1":
        add_contatos()
    
    elif opcao == "2":
        ver_contatos()
    
    elif opcao == "3":
        buscar_contato()

    elif opcao == "4":
        remover_contato()
    
    elif opcao == "5":
        editar_contato()
    
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida.")